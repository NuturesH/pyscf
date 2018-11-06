class QM_Region:
    # init class
    def __init__(self, name, chain_resid):
        self.name = name
        #self.chain = chain_resid.keys()
	self.chain_resid = chain_resid
        #self.resid = resid

    # write a pdb structure
    def write_pdb(self):
        from Bio.PDB.PDBParser import PDBParser
        from Bio.PDB import PDBIO
        from Peptide_Select import struc_select
        filename = self.name
        #chain = self.chain
	chain_resid = self.chain_resid
        #resid = self.resid
        p = PDBParser(PERMISSIVE = 1)
        struc_id = filename.split('.')[0]
        s = p.get_structure(struc_id, filename)
        out_filename = 'QM_region.pdb'
        io = PDBIO()
        io.set_structure(s)
        io.save(out_filename, struc_select(chain_resid))
dic_l = {'A':[100, 101], 'B': [100, 101]}
k = QM_Region('3WU2.pdb', dic_l)
k.write_pdb()
