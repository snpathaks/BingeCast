import joblib
import pandas as pd
import sys

def get_user_input():
    print("\n--- 🎬 BingeCast Predictor 🎬 ---")
    print("Answer the following to predict your next binge session:\n")
    
    try:
        age = int(input("Enter your Age: "))
    except ValueError:
        print("Invalid age entered.")
        sys.exit()

    print("\nSelect your Mood:")
    moods = ['Happy', 'Sad', 'Bored', 'Stressed', 'Energetic', 'Relaxed', 'Excited', 'Calm']
    for i, m in enumerate(moods, 1):
        print(f"{i}. {m}")
    mood_idx = int(input("Choice (1-8): ")) - 1
    mood = moods[mood_idx]

    print("\nSelect Preferred Genre:")
    genres = ['Comedy', 'Drama', 'Action', 'Sci-Fi', 'Animation', 'Documentary']
    for i, g in enumerate(genres, 1):
        print(f"{i}. {g}")
    genre_idx = int(input("Choice (1-6): ")) - 1
    genre = genres[genre_idx]

    print("\nSelect Time of Day:")
    times = ['Morning', 'Afternoon', 'Evening', 'Night']
    for i, t in enumerate(times, 1):
        print(f"{i}. {t}")
    time_idx = int(input("Choice (1-4): ")) - 1
    time_val = times[time_idx]

    return pd.DataFrame({
        'Age': [age],
        'Mood': [mood],
        'Preferred Genre': [genre],
        'Time of Day': [time_val]
    })

def main():
    
    try:
        model = joblib.load('bingecast_model.pkl')
    except FileNotFoundError:
        print("❌ Model file not found. Please run 'bingecast.py' first to train the model.")
        return

    
    user_data = get_user_input()
    
    
    prediction = model.predict(user_data)[0]
    
    print(f"\n🔮 Prediction: You will likely binge-watch {int(round(prediction))} episodes!")
    print("---------------------------------------")

if __name__ == "__main__":

    main()
