-- ALTER TABLE users
-- ADD COLUMN health_goals VARCHAR
-- select * from food_logs;
-- delete from food_logs;

-- INSERT INTO food_logs (
--     id,
--     servings,
--     date_logged,
--     calories,
--     protein,
--     carbs,
--     fats,
--     serving_unit,
--     serving_weight_grams,
--     meal_type,
--     food_name
--   )
-- VALUES (
--     id:integer,
--     'servings:double precision',
--     'date_logged:timestamp without time zone',
--     'calories:double precision',
--     'protein:double precision',
--     'carbs:double precision',
--     'fats:double precision',
--     'serving_unit:character varying',
--     serving_weight_grams:integer,
--     meal_type:integer,
--     'food_name:character varying'
--   );

INSERT INTO users_to_foods (user_id, food_id)
VALUES (1, 24);