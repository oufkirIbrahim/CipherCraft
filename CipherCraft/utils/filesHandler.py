
from .Generators.errorLogger import ErrorLogger


class FilesHandler:
    def __init__(self):

        # DEFINING ERROR LOGGER
        self.error_logger = ErrorLogger()

    def read_file(self, src) -> list[str]:
        """
        This Function Read File Content
        :param src:
        :return: str
        """
        content = None
        try:

            # OPENING FILE IN READONLY MODE
            with open(src, 'r') as file:

                # READING LINES
                content = ''.join(file.readlines())
        except Exception as e:

            # ERROR OCCURRED
            self.error_logger.error_log(e)
        finally:
            return content

    def write_file(self, dist, content, mode='w') -> bool:
        """
        This Function Writes To Files Destination
        :param mode:
        :param dist:
        :param content:
        :return: bool
        """

        try:

            # OPENING FILE IN WRITE MODE
            with open(dist, mode) as file:

                # WRITING TO FILE
                file.write(content)

                return True
        except Exception as e:

            # ERROR OCCURRED
            self.error_logger.error_log(e)
        finally:
            return False

    def append_file(self, dist, content) -> bool:
        """
        This Function appends Files
        :param dist:
        :param content:
        :return: bool
        """
        return self.write_file(dist, content, 'a')



