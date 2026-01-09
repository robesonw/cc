CREATE TABLE favorite_meal (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    meal_type TEXT NOT NULL CHECK (meal_type IN ('breakfast', 'lunch', 'dinner', 'snacks')),
    calories TEXT,
    protein DOUBLE PRECISION,
    carbs DOUBLE PRECISION,
    fat DOUBLE PRECISION,
    nutrients TEXT,
    prep_tip TEXT,
    prep_time TEXT,
    prep_steps JSONB,
    difficulty TEXT,
    equipment JSONB,
    health_benefit TEXT,
    image_url TEXT,
    cuisine TEXT,
    cooking_time TEXT,
    tags JSONB,
    source_type TEXT CHECK (source_type IN ('meal_plan', 'ai_recipe', 'shared_recipe', 'manual')),
    source_meal_plan_id TEXT,
    source_meal_plan_name TEXT,
    source_recipe_id TEXT,
    ingredients JSONB,
    grocery_list JSONB,
    estimated_cost DOUBLE PRECISION,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE feedback (
    id TEXT PRIMARY KEY,
    user_name TEXT,
    user_email TEXT,
    page TEXT,
    rating DOUBLE PRECISION,
    feedback_type TEXT NOT NULL CHECK (feedback_type IN ('bug', 'feature_request', 'general', 'praise')),
    message TEXT NOT NULL,
    status TEXT CHECK (status IN ('new', 'reviewed', 'resolved')),
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE nutrition_log (
    id TEXT PRIMARY KEY,
    recipe_name TEXT NOT NULL,
    meal_type TEXT CHECK (meal_type IN ('breakfast', 'lunch', 'dinner', 'snack')),
    log_date TEXT NOT NULL,
    calories DOUBLE PRECISION NOT NULL,
    protein DOUBLE PRECISION,
    carbs DOUBLE PRECISION,
    fat DOUBLE PRECISION,
    micronutrients JSONB,
    servings DOUBLE PRECISION,
    food_source TEXT CHECK (food_source IN ('manual', 'usda', 'open_food_facts')),
    food_id TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE shared_recipe (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    meal_type TEXT NOT NULL CHECK (meal_type IN ('breakfast', 'lunch', 'dinner', 'snacks')),
    description TEXT,
    meal_data JSONB NOT NULL,
    calories TEXT,
    protein DOUBLE PRECISION,
    carbs DOUBLE PRECISION,
    fat DOUBLE PRECISION,
    image_url TEXT,
    tags JSONB,
    views_count DOUBLE PRECISION,
    likes_count DOUBLE PRECISION,
    saves_count DOUBLE PRECISION,
    average_rating DOUBLE PRECISION,
    author_name TEXT,
    status TEXT CHECK (status IN ('pending', 'approved', 'rejected')),
    moderation_notes TEXT,
    cuisine TEXT,
    difficulty TEXT CHECK (difficulty IN ('Easy', 'Medium', 'Hard')),
    prep_time TEXT,
    cooking_time TEXT,
    servings DOUBLE PRECISION,
    ingredients JSONB,
    prep_steps JSONB,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE meal_plan (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    diet_type TEXT NOT NULL CHECK (diet_type IN ('liver-centric', 'low-sugar', 'vegetarian', 'custom')),
    cultural_style TEXT CHECK (cultural_style IN ('mediterranean', 'asian', 'indian', 'latin_american', 'african', 'middle_eastern', 'european', 'fusion', 'none')),
    life_stage TEXT CHECK (life_stage IN ('general', 'children', 'pregnancy', 'seniors')),
    days JSONB NOT NULL,
    preferences JSONB,
    macros JSONB,
    estimated_cost DOUBLE PRECISION,
    grocery_list JSONB,
    current_total_cost DOUBLE PRECISION,
    hero_image_url TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE forum_comment (
    id TEXT PRIMARY KEY,
    post_id TEXT NOT NULL,
    content TEXT NOT NULL,
    likes_count DOUBLE PRECISION,
    author_name TEXT,
    reactions JSONB,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE notification (
    id TEXT PRIMARY KEY,
    recipient_email TEXT NOT NULL,
    type TEXT NOT NULL CHECK (type IN ('new_follower', 'plan_comment', 'recipe_comment', 'plan_like', 'recipe_like', 'forum_reply')),
    title TEXT NOT NULL,
    message TEXT NOT NULL,
    link TEXT,
    is_read BOOLEAN,
    actor_name TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE user_follow (
    id TEXT PRIMARY KEY,
    following_user_email TEXT NOT NULL,
    following_user_name TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE shared_progress (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    progress_type TEXT NOT NULL CHECK (progress_type IN ('streak', 'goal_reached', 'milestone', 'weekly_summary')),
    stats JSONB,
    date_range JSONB,
    likes_count DOUBLE PRECISION,
    comments_count DOUBLE PRECISION,
    author_name TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE shared_meal_plan (
    id TEXT PRIMARY KEY,
    original_plan_id TEXT,
    title TEXT NOT NULL,
    description TEXT,
    plan_data JSONB NOT NULL,
    diet_type TEXT,
    cultural_style TEXT,
    tags JSONB,
    views_count DOUBLE PRECISION,
    likes_count DOUBLE PRECISION,
    saves_count DOUBLE PRECISION,
    average_rating DOUBLE PRECISION,
    author_name TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE progress_comment (
    id TEXT PRIMARY KEY,
    progress_id TEXT NOT NULL,
    comment TEXT NOT NULL,
    author_name TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE nutrition_goal (
    id TEXT PRIMARY KEY,
    goal_type TEXT NOT NULL CHECK (goal_type IN ('daily', 'weekly')),
    target_calories DOUBLE PRECISION,
    target_protein DOUBLE PRECISION,
    target_carbs DOUBLE PRECISION,
    target_fat DOUBLE PRECISION,
    target_micronutrients JSONB,
    is_active BOOLEAN,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE user_preferences (
    id TEXT PRIMARY KEY,
    age DOUBLE PRECISION,
    gender TEXT CHECK (gender IN ('male', 'female', 'other')),
    height DOUBLE PRECISION,
    weight DOUBLE PRECISION,
    health_goal TEXT CHECK (health_goal IN ('liver_health', 'weight_loss', 'blood_sugar_control', 'muscle_gain', 'heart_health', 'kidney_health', 'digestive_health', 'energy_boost', 'immune_support', 'anti_inflammatory', 'bone_health', 'general_wellness')),
    dietary_restrictions TEXT,
    foods_liked TEXT,
    foods_avoided TEXT,
    allergens JSONB,
    cuisine_preferences JSONB,
    cooking_time TEXT CHECK (cooking_time IN ('any', 'under_15', '15_30', '30_60', 'over_60')),
    skill_level TEXT CHECK (skill_level IN ('beginner', 'intermediate', 'advanced')),
    num_people DOUBLE PRECISION,
    weekly_budget DOUBLE PRECISION,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE user_settings (
    id TEXT PRIMARY KEY,
    email_notifications BOOLEAN,
    recipe_approved_notifications BOOLEAN,
    recipe_rejected_notifications BOOLEAN,
    new_follower_notifications BOOLEAN,
    comment_notifications BOOLEAN,
    like_notifications BOOLEAN,
    weekly_summary BOOLEAN,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE grocery_list (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    items JSONB,
    total_cost DOUBLE PRECISION,
    notes TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE review (
    id TEXT PRIMARY KEY,
    target_id TEXT NOT NULL,
    target_type TEXT NOT NULL CHECK (target_type IN ('meal_plan', 'shared_plan')),
    rating DOUBLE PRECISION NOT NULL,
    comment TEXT,
    helpful_count DOUBLE PRECISION,
    author_name TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE recipe_comment (
    id TEXT PRIMARY KEY,
    recipe_id TEXT NOT NULL,
    comment TEXT NOT NULL,
    author_name TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE forum_post (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    category TEXT NOT NULL CHECK (category IN ('general', 'recipes', 'nutrition', 'meal_prep', 'tips', 'questions')),
    tags JSONB,
    likes_count DOUBLE PRECISION,
    views_count DOUBLE PRECISION,
    comments_count DOUBLE PRECISION,
    is_pinned BOOLEAN,
    author_name TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE lab_result (
    id TEXT PRIMARY KEY,
    upload_date TEXT NOT NULL,
    file_url TEXT,
    biomarkers JSONB,
    notes TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE user_interaction (
    id TEXT PRIMARY KEY,
    target_id TEXT NOT NULL,
    target_type TEXT NOT NULL CHECK (target_type IN ('shared_plan', 'forum_post', 'forum_comment')),
    interaction_type TEXT NOT NULL CHECK (interaction_type IN ('like', 'save', 'view')),
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
