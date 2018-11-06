from Bio.PDB.PDBIO import Select
class struc_select(Select):
	def __init__(self, chains_resids):
		self.chains = chains_resids.keys()
		self.chains_resids = chains_resids
	def accept_residue(self, residue):
		chains_resids = self.chains_resids
		chain = residue.get_full_id()[2]
		res_id = residue.get_id()[1]
		if chain in self.chains and res_id in chains_resids[chain]:
			return True
		else:
			return False
