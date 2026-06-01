from flask import Blueprint
from controller.tokenized_data_learnsanskrit_controller import add_new_story,fetch_all_tokenized_stories,fetch_tokenized_story_by_id,fetch_tokenized_stories_by_category

from flasgger import swag_from


tokenize_data_bp = Blueprint("tokenize_data_bp",__name__)



#Post route that will take an id retrieve data from learn sanskrit.cc tokenize it and store it in data folder

add_new_story_controller = swag_from("../swaggerdocs/tokenized_data/add_new_story_learnsanskrit.yml")(add_new_story)
tokenize_data_bp.route("/addNew",methods=["POST"])(add_new_story_controller)


get_all_tokenized_controller = swag_from("../swaggerdocs/tokenized_data/get_all_tokenized_stories.yml")(fetch_all_tokenized_stories)
## Get all tokenized stories
tokenize_data_bp.route("/getAllTokenized",methods=["GET"])(get_all_tokenized_controller)


get_tokenized_by_id_controller = swag_from("../swaggerdocs/tokenized_data/get_tokenized_story_by_id.yml")(fetch_tokenized_story_by_id)
## Get tokenized story by Id
tokenize_data_bp.route("/getTokenizedById",methods=["GET"])(get_tokenized_by_id_controller)

tokenize_data_bp.route("/getByCategory", methods=["GET"])(fetch_tokenized_stories_by_category)