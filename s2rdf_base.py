import abc

class S2rdfBase(abc.ABC):

    @classmethod
    @abc.abstractmethod
    def load_rdf(input_rdf, spark_cluster, path_to_jar, scale = 0.25):
        # SPARK job: input file (RDF), output(db) directory, jarFilePath, spark cluster
  	    """This function will load an rdf file into the S2RDF format (VP and ExtVP) into the HDFS 

        Args:
            param1 (str): Input RDF File.
            param2 (str): ExtVP scale (optional; default = 0.25).
  			    param2 (str): Spark cluster
            param2 (str): Path to Jar file of S2RDF	Loader			

            Returns:
                nothing - Files will be saved at VP/ and ExtVP/. (May make this an method argument)
        """
  	    pass

    @classmethod
    @abc.abstractmethod
    def sparql_translator(input_sparql, output_dir, spark_cluster, path_to_jar):
  			"""This function will translate a SPARQL query into a SQL query

        Args:
            param1 (str): Input SPARQL File.
            param2 (str): output sql directory
  			    param2 (str): Spark cluster
            param2 (str): Path to Jar file of S2RDF	Query Translator			

            Returns:
                nothing - Files will be saved in the output directory.
        """
        pass

    @classmethod
    @abc.abstractmethod
    def query_executor(db_dir, query_file, spark_cluster, jarFilePath):
				"""This function will execute a Spark SQL query

        Args:
            param1 (str): database directory.
            param2 (str): query list file
  			    param2 (str): Spark cluster
            param2 (str): Path to Jar file of S2RDF	Query Translator			

            Returns:
                nothing - Files will be saved in the output directory.
        """
  	    pass

