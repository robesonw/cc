from fastapi import FastAPI
from app.api.health import router as health_router

app = FastAPI(title="Generated Backend API", version="0.1.0")

app.include_router(health_router, prefix="/api")

from app.api.entities.favorite_meal import router as favorite_meal_router
app.include_router(favorite_meal_router, prefix="/api/favorite-meal", tags=["FavoriteMeal"])

from app.api.entities.feedback import router as feedback_router
app.include_router(feedback_router, prefix="/api/feedback", tags=["Feedback"])

from app.api.entities.forum_comment import router as forum_comment_router
app.include_router(forum_comment_router, prefix="/api/forum-comment", tags=["ForumComment"])

from app.api.entities.forum_post import router as forum_post_router
app.include_router(forum_post_router, prefix="/api/forum-post", tags=["ForumPost"])

from app.api.entities.grocery_list import router as grocery_list_router
app.include_router(grocery_list_router, prefix="/api/grocery-list", tags=["GroceryList"])

from app.api.entities.lab_result import router as lab_result_router
app.include_router(lab_result_router, prefix="/api/lab-result", tags=["LabResult"])

from app.api.entities.meal_plan import router as meal_plan_router
app.include_router(meal_plan_router, prefix="/api/meal-plan", tags=["MealPlan"])

from app.api.entities.notification import router as notification_router
app.include_router(notification_router, prefix="/api/notification", tags=["Notification"])

from app.api.entities.nutrition_goal import router as nutrition_goal_router
app.include_router(nutrition_goal_router, prefix="/api/nutrition-goal", tags=["NutritionGoal"])

from app.api.entities.nutrition_log import router as nutrition_log_router
app.include_router(nutrition_log_router, prefix="/api/nutrition-log", tags=["NutritionLog"])

from app.api.entities.progress_comment import router as progress_comment_router
app.include_router(progress_comment_router, prefix="/api/progress-comment", tags=["ProgressComment"])

from app.api.entities.recipe_comment import router as recipe_comment_router
app.include_router(recipe_comment_router, prefix="/api/recipe-comment", tags=["RecipeComment"])

from app.api.entities.review import router as review_router
app.include_router(review_router, prefix="/api/review", tags=["Review"])

from app.api.entities.shared_meal_plan import router as shared_meal_plan_router
app.include_router(shared_meal_plan_router, prefix="/api/shared-meal-plan", tags=["SharedMealPlan"])

from app.api.entities.shared_progress import router as shared_progress_router
app.include_router(shared_progress_router, prefix="/api/shared-progress", tags=["SharedProgress"])

from app.api.entities.shared_recipe import router as shared_recipe_router
app.include_router(shared_recipe_router, prefix="/api/shared-recipe", tags=["SharedRecipe"])

from app.api.entities.user_follow import router as user_follow_router
app.include_router(user_follow_router, prefix="/api/user-follow", tags=["UserFollow"])

from app.api.entities.user_interaction import router as user_interaction_router
app.include_router(user_interaction_router, prefix="/api/user-interaction", tags=["UserInteraction"])

from app.api.entities.user_preferences import router as user_preferences_router
app.include_router(user_preferences_router, prefix="/api/user-preferences", tags=["UserPreferences"])

from app.api.entities.user_settings import router as user_settings_router
app.include_router(user_settings_router, prefix="/api/user-settings", tags=["UserSettings"])
