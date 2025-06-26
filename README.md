# 🐾 Animal Web Generator

A simple Python project that fetches animal data from the [API Ninjas Animals API](https://api-ninjas.com/api/animals) and generates a styled HTML webpage. Ideal for learning, educational projects, or anyone interested in combining Python with web development and real-world APIs.

---

## 🔧 Features

- Live animal data retrieval via API Ninjas
- Dynamic HTML generation using a template
- Clean separation between data logic (`data_fetcher.py`) and web generation (`animals_web_generator.py`)
- Graceful error handling and informative fallback messages

---

## 📸 Sample Output

```html
<li class="cards__item">
  <div class="card__title">Lion</div>
  <div class="card__text">
    <ul>
      <li><strong>Diet:</strong> Carnivore</li>
      <li><strong>Location:</strong> Africa</li>
      <li><strong>Type:</strong> Mammal</li>
      <li><strong>Class:</strong> Mammalia</li>
      <li><strong>Name of young:</strong> Cub</li>
      <li><strong>Lifespan:</strong> 10-14 years</li>
      ...
    </ul>
  </div>
</li>
```

---

## 🚀 Installation

### 1. Clone the repository
```
git clone https://github.com/aline-j/my-zootopia-with-api.git
cd animal-web-generator
```

### 2. (Optional) Create a virtual environment
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Create your .env file
Create a .env file in the root directory and add your API key like this:
```
API_NINJAS_KEY=your_api_key_here
```
You can get a free API key from: https://api-ninjas.com/register


---

## 🧪 How to Use
```
python animals_web_generator.py
```
You will be prompted to enter an animal name.
The script then generates an animals.html file containing relevant information.

Open animals.html in your browser to view the result.


---

## 📁 Project Structure

```plaintext
.
├── animals_template.html       # HTML template with placeholder
├── animals.html                # Generated HTML file
├── animals_web_generator.py    # Main script
├── data_fetcher.py             # API logic
├── .env                        # API key (not to be committed)
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## ⚖️ License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).  
Animal data is provided by [API Ninjas](https://api-ninjas.com/api/animals) and is subject to their [terms of use](https://api-ninjas.com/terms).  
Please respect their **fair use policy** when using the API.
