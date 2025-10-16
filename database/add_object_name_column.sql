-- Add object_name column to detections table
ALTER TABLE detections ADD COLUMN object_name VARCHAR(50);

-- Update existing records with object names
UPDATE detections 
SET object_name = ot.type_name 
FROM object_types ot 
WHERE detections.type_id = ot.type_id;