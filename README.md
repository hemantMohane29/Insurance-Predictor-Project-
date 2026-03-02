# Medical Expense Predictor

A Django-based web application that predicts medical insurance costs using machine learning. The application uses a Linear Regression model trained on demographic and health factors to estimate annual medical expenses.

## Features

- **AI-Powered Predictions**: Uses scikit-learn Linear Regression model for accurate cost estimation
- **Beautiful UI**: Modern, responsive interface with gradient design
- **Real-time Predictions**: Instant results based on user input
- **Comprehensive Factors**: Considers age, BMI, smoking status, number of children, gender, and region
- **Detailed Results**: Shows predicted annual costs, monthly estimates, risk level, and health score

## Tech Stack

- **Backend**: Django 5.2.9
- **Machine Learning**: scikit-learn, pandas, numpy, joblib
- **Frontend**: HTML5, CSS3, JavaScript
- **Server**: Gunicorn
- **Static Files**: WhiteNoise
- **Deployment**: Railway / Render

## Project Structure

```
insurance-predictor/
├── app/                          # Main Django app
│   ├── models/                   # ML model files
│   │   └── linear_regression_model.pkl
│   ├── views.py                  # View logic
│   ├── urls.py                   # URL routing
│   └── ...
├── insurance/                    # Django project settings
│   ├── settings.py              # Configuration
│   ├── urls.py                  # Main URL config
│   └── wsgi.py                  # WSGI config
├── templates/                    # HTML templates
│   ├── base.html                # Base template with styling
│   └── index.html               # Main form template
├── static/                       # Static files
├── linear_regression_model.pkl  # Trained ML model
├── model_columns.pkl            # Model feature columns
├── insurance.csv                # Training data
├── train_model.py               # Model training script
├── requirements.txt             # Python dependencies
├── Procfile                     # Deployment config
├── nixpacks.toml               # Railway build config
└── manage.py                    # Django management

```

## Installation & Setup

### Prerequisites
- Python 3.11+
- pip
- Git

### Local Development

1. **Clone the repository**
```bash
git clone https://github.com/hemantMohane29/Insurance-Predictor-Project-.git
cd Insurance-Predictor-Project-
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run migrations**
```bash
python manage.py migrate
```

5. **Collect static files**
```bash
python manage.py collectstatic --no-input
```

6. **Run development server**
```bash
python manage.py runserver
```

7. **Access the application**
Open your browser and navigate to `http://localhost:8000`

## Model Training

The machine learning model is already trained and included in the repository. If you want to retrain the model:

```bash
python train_model.py
```

This will:
- Load data from `insurance.csv`
- Train a Linear Regression model
- Save the model to `linear_regression_model.pkl`
- Save feature columns to `model_columns.pkl`

## Deployment

### Deploy to Railway

1. **Push to GitHub**
```bash
git add .
git commit -m "Ready for deployment"
git push origin master
```

2. **Deploy on Railway**
   - Go to [railway.app](https://railway.app)
   - Sign in with GitHub
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your repository
   - Railway will automatically detect and deploy using `nixpacks.toml`

3. **Generate Domain**
   - Go to project settings
   - Click "https://web-production-00dd.up.railway.app/" to get a public URL

### Deploy to Render

1. **Push to GitHub** (same as above)

2. **Deploy on Render**
   - Go to [render.com](https://render.com)
   - Click "New" → "Web Service"
   - Connect your GitHub repository
   - Render will use `render.yaml` for configuration

## Environment Variables

For production deployment, set these environment variables:

- `SECRET_KEY`: Django secret key (generate a new one for production)
- `DJANGO_DEBUG`: Set to `false` for production
- `DJANGO_ALLOWED_HOSTS`: Your domain (comma-separated)
- `DJANGO_CSRF_TRUSTED_ORIGINS`: Trusted origins for CSRF (comma-separated)

## Usage

1. **Enter Patient Details**:
   - Age (0-120)
   - BMI (Body Mass Index, 10-60)
   - Number of children/dependents
   - Smoking status (Yes/No)
   - Region (Northwest, Northeast, Southwest, Southeast)
   - Gender (Male/Female)

2. **Click "Calculate Prediction"**

3. **View Results**:
   - Predicted annual medical expenses
   - Monthly cost estimate
   - Risk level assessment
   - Health score

## Model Information

- **Algorithm**: Linear Regression
- **Features**: Age, BMI, Children, Gender, Smoking Status, Region
- **Accuracy**: ~94% (based on training data)
- **Training Data**: Insurance dataset with demographic and cost information

## API Endpoints

- `GET /` - Home page with prediction form
- `POST /` - Submit form and get prediction

## Dependencies

```
Django==5.2.9
gunicorn==23.0.0
whitenoise==6.8.2
scikit-learn==1.6.1
pandas==2.2.3
numpy==2.2.3
joblib==1.4.2
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Disclaimer

This tool provides estimates based on statistical models and should not replace professional medical or financial advice. Actual medical expenses may vary based on individual circumstances, healthcare provider rates, and insurance coverage.

## Author

**Hemant Mohane**
- GitHub: [@hemantMohane29](https://github.com/hemantMohane29)

## Acknowledgments

- Dataset source: Insurance cost prediction dataset
- Built with Django and scikit-learn
- Deployed on Railway

## Support

For issues, questions, or contributions, please open an issue on GitHub.

---

Made with ❤️ by Hemant Mohane
