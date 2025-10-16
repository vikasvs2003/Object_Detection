-- Create a view for easy viewing of detected objects
CREATE OR REPLACE VIEW detected_objects AS
SELECT 
    object_id,
    object_name,
    confidence_score,
    timestamp,
    latitude,
    longitude,
    image_reference
FROM detections 
WHERE object_name IS NOT NULL
ORDER BY object_id DESC;

-- Create summary view by object type
CREATE OR REPLACE VIEW object_summary AS
SELECT 
    object_name,
    COUNT(*) as total_detections,
    AVG(confidence_score) as avg_confidence,
    MAX(confidence_score) as max_confidence,
    MIN(timestamp) as first_detected,
    MAX(timestamp) as last_detected
FROM detections 
WHERE object_name IS NOT NULL
GROUP BY object_name
ORDER BY total_detections DESC;