from src.models import *

class DatabaseManager:
    """
    Allows manage the database
    """
    MODELS = [Category]

    def __init__(self):
        """
        Initialize the database manager
        """
        self.createTables()
    
    def createTables(self):
        """
        Creates the tables in the database
        """
        with database:
            database.create_tables(self.MODELS)

    def dropTables(self):
        """
        Deletes the tables in the database
        """
        with database:
            database.drop_tables(self.MODELS)
    
    def cleanUp(self):
        """
        Clean up the database
        """
        self.dropTables()
        self.createTables()

class CategoryManager:
    """
    Allows manage the categories
    """

    def loadCategories(self, categories):
        """
        Loads given categories in the database

        :param categories: iterable
        """
        with database.atomic():
            for data in categories:
                category = {
                    'id': data.get('CategoryID'),
                    'name': data.get('CategoryName'),
                    'level': data.get('CategoryLevel'),
                    'bestOfferEnabled': data.get('BestOfferEnabled', False),
                    'parent': data.get('CategoryParentID', None)
                }

                if category['id'] == category['parent']:
                    category['parent'] = None

                Category.create(**category)
    
    def getById(self, id):
        """
        Fetch category by given id

        :param id: integer
        """
        return Category.get_by_id(id)
    
    def getByParentId(self, parentId):
        """
        Fetch categories that "parent" identifier is equal to given parentId

        :param parentId: integer
        """
        Parent = Category.alias()
        return (Category
            .select(Category, Parent)
            .join(Parent, on=(Category.parent == Parent.id))
            .where(Parent.id == parentId))