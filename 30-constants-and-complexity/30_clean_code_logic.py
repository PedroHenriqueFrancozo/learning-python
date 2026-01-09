"""
Topic: Constants and Code Complexity
Focus: Refactoring logic to improve readability and maintainability.
"""

# CONSTANTS = "Variables" that should not change (Use UPPER_CASE)
# Too many conditions in the same IF = Bad (High complexity)
# Clean code principle: Give names to logical expressions

speed = 61  # Current car speed
car_location = 100  # Current location on the highway

RADAR_1 = 60  # Maximum speed allowed for Radar 1
LOCAL_1 = 100  # Location where Radar 1 is positioned
RADAR_RANGE = 1  # Detection range before and after the radar location

# Descriptive variables for logical conditions
# This reduces "Cognitive Complexity"
car_speed_exceeded_radar_1 = speed > RADAR_1

car_is_at_radar_1_range = (
    car_location >= (LOCAL_1 - RADAR_RANGE) and 
    car_location <= (LOCAL_1 + RADAR_RANGE)
)

car_fined_at_radar_1 = car_is_at_radar_1_range and car_speed_exceeded_radar_1

if car_speed_exceeded_radar_1:
    print('Car speed exceeded Radar 1 limit')

if car_is_at_radar_1_range:
    print('Car passed through Radar 1 range')

if car_fined_at_radar_1:
    print('Car was fined at Radar 1')