import pandas as pd
import numpy as np
import random

def create_synthetic_data(num_samples=1000):
    np.random.seed(42)
    
    data = []
    
    for _ in range(num_samples):
        
        age = np.random.randint(13, 65)
        
        
        if 13 <= age <= 17:
            
            genre = 'Animation'
            mood = np.random.choice(['Happy', 'Excited'])
            time = np.random.choice(['Afternoon', 'Evening'])
            base_episodes = 4  
            
        elif 18 <= age <= 29:
            
            genre = 'Action'
            mood = np.random.choice(['Happy', 'Energetic'])
            time = np.random.choice(['Evening', 'Night'])
            base_episodes = 3
            
        elif 30 <= age <= 44:
            
            genre = 'Drama'
            mood = np.random.choice(['Relaxed', 'Happy'])
            time = np.random.choice(['Evening', 'Night'])
            base_episodes = 2
            
        else: 
            
            genre = 'Documentary'
            mood = np.random.choice(['Relaxed', 'Calm'])
            time = np.random.choice(['Morning', 'Afternoon'])
            base_episodes = 1

        
        if time == 'Night':
            base_episodes += 1
        if mood in ['Excited', 'Energetic']:
            base_episodes += 1
            
       
        episodes = max(1, int(base_episodes + np.random.normal(0, 1)))

        data.append({
            'Age': age,
            'Mood': mood,
            'Preferred Genre': genre,
            'Time of Day': time,
            'Episodes': episodes
        })
    
    return pd.DataFrame(data)

if __name__ == "__main__":
    print("Generating synthetic data based on CSV patterns...")
    df = create_synthetic_data(1000)
    
    output_file = 'bingecast_dataset.csv'
    df.to_csv(output_file, index=False)
    
    print(f"✅ Data saved to {output_file}")
    print("\nFirst 5 rows:")

    print(df.head())
