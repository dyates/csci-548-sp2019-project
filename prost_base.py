import abc

class SparqlOverSpark(abc.ABC):

	# Any shared data strcutures or methods should be defined as part of the parent class.
	
	# A list of shared arguments should be defined for each of the following methods and replace (or precede) *args.
	
	# The output of each of the following methods should be defined clearly and shared between all methods implemented by members of the group. 

    @classmethod
    @abc.abstractmethod
    def load_rdf(input_rdf, output_dir, spark_cluster, path_to_jar):
        """This function will load an rdf file into the PROST format (VP and Property Table) into the HDFS 
            Args:
                param1 (str): Input RDF File.
                param2 (str): output directory
                param2 (str): Path to Jar file of PROST	Loader			

            Returns:
                nothing - Files will be saved in output directory on HDFS
        """
        pass

    @classmethod
    @abc.abstractmethod
    def query_executor(spaql_query_file, db_dir, output_dir, spark_cluster, path_to_jar):
        """This function will execute a Spark SQL query

        Args:
            param1 (str): SPARQL query file
            param1 (str): database directory. 
            param3 (str): output directory           
  			param2 (str): Spark cluster
            param2 (str): Path to Jar file of PROST	Query Executor			

            Returns:
                nothing - Files will be saved in the output directory.
        """
        pass