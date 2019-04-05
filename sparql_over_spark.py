import abc

class SparqlOverSpark(abc.ABC):

	# Any shared data strcutures or methods should be defined as part of the parent class.
	
	# A list of shared arguments should be defined for each of the following methods and replace (or precede) *args.
	
	# The output of each of the following methods should be defined clearly and shared between all methods implemented by members of the group. 
	
	@classmethod
	@abc.abstractmethod
    # SPARK job: input file (RDF), output(db) directory, jarFilePath, spark cluster
	def load_rdf(*args, **kwargs):
		pass

	@classmethod
	@abc.abstractmethod
    # SPARK job: input file (SPARQL query), query db directory, jarFilePath, spark cluster
	def query_executor(*args, **kwargs):
		pass
