-- Object Types lookup table
CREATE TABLE object_types (
    type_id SERIAL PRIMARY KEY,
    type_name VARCHAR(50) UNIQUE NOT NULL
);

-- Main detections table
CREATE TABLE detections (
    object_id SERIAL PRIMARY KEY,
    type_id INTEGER REFERENCES object_types(type_id),
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8),
    confidence_score DECIMAL(5, 4) CHECK (confidence_score >= 0 AND confidence_score <= 1),
    image_reference VARCHAR(255)
);

-- Indexes for fast queries
CREATE INDEX idx_detections_type_id ON detections(type_id);
CREATE INDEX idx_detections_timestamp ON detections(timestamp);
CREATE INDEX idx_detections_location ON detections(latitude, longitude);
CREATE INDEX idx_detections_confidence ON detections(confidence_score DESC);

-- Insert common object types
INSERT INTO object_types (type_name) VALUES 
('person'), ('bicycle'), ('car'), ('motorcycle'), ('airplane'),
('bus'), ('train'), ('truck'), ('boat'), ('traffic light'),
('fire hydrant'), ('stop sign'), ('parking meter'), ('bench'),
('bird'), ('cat'), ('dog'), ('horse'), ('sheep'), ('cow');