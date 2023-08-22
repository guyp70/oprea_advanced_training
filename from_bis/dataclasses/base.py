

class Transactional:
    """
    Wraps an object and allow to rollback changes done to it.
    """
	
    def __init__(self, target):
        """
        Create a  Transactional object.

        :param target: The object to wrap.
        :type target: object
        """
        raise NotImplementedError()

    def rollback(self):
        """
        Rollback all changes done to object.
        """
        raise NotImplementedError()

    def commit(self):
        """
        Commit all changes to object.
        """
        raise NotImplementedError()
