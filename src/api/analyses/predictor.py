from helpers import load_json
import subprocess
import os

class PredictorTaskManager():

	def __init__(self, outdir):
		self.outdir=outdir

	def run_predictor(self, file, sample_id):
	    cmd="mykrobe predict {sample_id} tb -1 {file} --output {sample_id}.json".format(sample_id=sample_id,file=file)
	    outfile=os.path.join(self.outdir, "{sample_id}.json".format(sample_id=sample_id))
	    out=subprocess.check_output(['mykrobe','predict', sample_id, "tb","--panel","atlas", "-1", file, "--output", outfile ])
	    ## Load the output
	    results=load_json(outfile)	
	    return results

	def run_genotype(self, file, sample_id):
	    cmd="mykrobe genotype {sample_id} data/tb-k21-probe-set-feb-09-2017.fasta.gz -1 {file} --output {sample_id}_gt.json".format(sample_id=sample_id,file=file)
	    outfile=os.path.join(self.outdir, "{sample_id}.json".format(sample_id=sample_id))
	    out=subprocess.check_output(['mykrobe','predict', sample_id, "tb","--panel","atlas", "-1", file, "--output", outfile ])
	    ## Load the output
	    results=load_json(outfile)	
	    return results	    
