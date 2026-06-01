from repository.get_all_tokenized_stories_learnsanskrit import GetAllTokenizedStories
from repository.get_all_tokenized_stories_from_mongodb import GetAllTokenizedStoriesFromMongoDB

class RetrieveTokenizedStories:

    def get_all(self):
        try:
            # # using the file system
            # data = GetAllTokenizedStories().get_all_stories()
            
            repo = GetAllTokenizedStoriesFromMongoDB()
            data = repo.get_all()

            return {
                "success": True,
                "data": data
            }

        except Exception as e:
            return {
                "success": False,
                "message": str(e)
            }