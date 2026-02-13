# 👗 Personalized Fashion Recommender

> **Note:** This project uses Deep Learning (CNN) to suggest fashion items based on visual similarity.

---

## 💬 How it Works (The Chat Guide)

**🤖 Assistant:** Hi Kiran! I see you've built a Fashion Recommender. How does it help users?

**👤 User:** It helps users find clothes similar to what they already like! You just upload a photo of a shirt or dress, and the system finds matches from the database.

**🤖 Assistant:** That's cool! What's under the hood? Is it using simple image processing?

**👤 User:** Not at all. I'm using **Deep Learning**. Specifically, the **ResNet50** model (pre-trained on ImageNet) to extract high-level features from the clothes.

**🤖 Assistant:** And how do you find the "closest" match once you have those features?

**👤 User:** I use **Euclidean Distance** and **Nearest Neighbors**. It compares the feature vector of your uploaded image against thousands of images in my dataset to find the top 5 closest matches.

**🤖 Assistant:** Impressive. What tools did you use to build the interface?

**👤 User:** I built the UI using **Streamlit**, so it's very interactive and easy to use in a browser!

---

## 🛠️ Tech Stack
* **Model:** ResNet50 (Transfer Learning)
* **Library:** TensorFlow / Keras
* **UI:** Streamlit
* **Search:** Scikit-learn (NearestNeighbors)

## 🚀 Quick Start
1. Clone the repo: `git clone https://github.com/KiranYadav-Bob/Personalized-Fashion-recommender.git`
2. Install requirements: `pip install -r requirements.txt`
3. Run the app: `streamlit run app.py`
