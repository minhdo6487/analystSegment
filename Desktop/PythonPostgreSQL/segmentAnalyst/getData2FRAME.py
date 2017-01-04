import graphlab
class callLoadData:
    loadData = None

    @classmethod
    def initialize(cls):
        cls.loadData = graphlab.SFrame('amazon_baby.gl')
        return cls.loadData

