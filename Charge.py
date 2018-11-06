

class chag_clu :
	def __init__(self, filename):
		self.filename = filename
		self.charge_site = []
		self.coord = []
		self.charge = []
	# add H for pdb
	def add_H(self):
		add_H_order = 'reduce %s.pdb %s_H.pdb'
	# calculation point chager using amber
	def point_charge(self):
		import os
		name = self.filename.split('.')[0]
		# replace model file 
		sed_order = "sed -i 's\model\%s\g' amber_model.dat" %name
		#print sed_order
		os.system(sed_order) 
		# using amber to generatr prmtop file and inpcrd file
		top_order = "tleap -f amber_model.dat"
		os.system(top_order)
		#restore model file
		sed_order = "sed -i 's\%s\model\g' amber_model.dat" %name
		os.system(sed_order)
		# calculation chager
		amber_order = "parmed.py ../data/%s.promtop ../data/parmed.in > ../data/%s.out" %(name, name)
		#print amber_order
		os.system(amber_order)
		# get point charge
		outfile_line_number = "wc -l ../data/%s.out | awk '{print $1}' " %name
		end = int(os.popen(outfile_line_number).read()) - 2
		pdbfile_line_number = "wc -l ../data/%s.pdb | awk '{print $1}' " %name
		start = end - int(os.popen(pdbfile_line_number).read()) - 3
		index_col = "sed -n '%d, %dp' ../data/%s.out | awk {'print $9'}" %(start, end, name)
		print index_col
		self.charge = os.popen(index_col).read()
	# combination charge input file format
	def comb_format(self):
		import numpy as np
		fp = open('test.dat', 'w')
		from Bio.PDB.PDBParser import PDBParser
		p = PDBParser(PERMISSIVE = 1)
		struc_id = self.filename
		filename = '../data/%s.pdb' %self.filename
		s = p.get_structure(struc_id, filename)
		atoms = s.get_atoms()
		number = 0
		for atom in atoms:
			line = np.append(atom, self.charge[number])
			number += 1
			fp.write(line + '\n')
		fp.close()
Point_Charge = chag_clu('QM_region')
Point_Charge.point_charge()
Point_Charge.comb_format()
