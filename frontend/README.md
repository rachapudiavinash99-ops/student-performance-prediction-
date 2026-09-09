# Student Performance Prediction - Frontend

Student Performance Prediction is a comprehensive, production-quality React frontend application designed for the comparative analysis of machine learning models for predicting student performance. It allows educators and administrators to upload datasets, train various ML models, compare their performance metrics, identify at-risk students, and generate explainability reports.

## Features
- **Dataset Management:** Upload and preview student performance datasets.
- **Model Training:** Train multiple classification and regression models (Random Forest, SVM, XGBoost, etc.).
- **Model Comparison:** Interactive charts and tables comparing accuracy, precision, F1 score, and training time.
- **Student Prediction:** Predict individual student performance based on multiple features.
- **Risk Analysis:** Identify and monitor at-risk students with a dedicated tracking dashboard.
- **Explainability:** View feature importance to understand why certain predictions were made.
- **Reports:** Generate and export PDF/CSV reports.

## Technology Stack
- **Framework:** React + TypeScript + Vite
- **Styling:** Tailwind CSS + Lucide React
- **Routing:** React Router DOM
- **Charts:** Recharts
- **Forms & Validation:** React Hook Form + Zod
- **API Client:** Axios

## Prerequisites
- Node.js (v20 or higher)
- npm (v10 or higher)

## Installation & Setup (Windows)

1. **Clone or Navigate to the project directory:**
   ```powershell
   cd Student Performance Prediction-frontend
   ```

2. **Install dependencies:**
   ```powershell
   npm install
   ```

## Environment Variables

Create a `.env` file in the root directory (you can copy `.env.example` if available) and add the following:

```env
VITE_API_BASE_URL=http://localhost:8000/api
```

*(Note: Currently, the frontend runs with realistic mock data if the backend is not connected).*

## Running the Frontend

To start the development server:

```powershell
npm run dev
```

The application will be accessible at `http://localhost:5173`.

## Connecting to the FastAPI Backend

1. Ensure your FastAPI server is running locally (e.g., `uvicorn main:app --reload --port 8000`).
2. Make sure the backend supports CORS for `http://localhost:5173`.
3. The Axios API client will automatically direct requests to `VITE_API_BASE_URL`.

## Building for Production

To create a production build:

```powershell
npm run build
```

This will output optimized static files to the `dist/` directory.

To preview the production build locally:

```powershell
npm run preview
```

## Troubleshooting

- **Dependency Errors (Vite/Rolldown):** If you see errors related to missing native bindings or EBADENGINE on Windows, try running `npm cache clean --force` followed by removing `node_modules` and re-running `npm install`.
- **TypeScript Unused Variables:** Unused variable linting is currently relaxed for faster development speed. You can re-enable it in `tsconfig.app.json` by setting `"noUnusedLocals": true`.
