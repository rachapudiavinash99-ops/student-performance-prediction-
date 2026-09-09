import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Layout from './components/common/Layout';
import Dashboard from './pages/Dashboard';
import DatasetManagement from './pages/DatasetManagement';
import ModelTraining from './pages/ModelTraining';
import ModelComparison from './pages/ModelComparison';
import StudentPrediction from './pages/StudentPrediction';
import SemesterPrediction from './pages/SemesterPrediction';
import AttendancePrediction from './pages/AttendancePrediction';
import RiskAnalysis from './pages/RiskAnalysis';
import Explainability from './pages/Explainability';
import Reports from './pages/Reports';
import Settings from './pages/Settings';
import Login from './pages/Login';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/" element={<Layout />}>
          <Route index element={<Navigate to="/dashboard" replace />} />
          <Route path="dashboard" element={<Dashboard />} />
          <Route path="datasets" element={<DatasetManagement />} />
          <Route path="training" element={<ModelTraining />} />
          <Route path="comparison" element={<ModelComparison />} />
          <Route path="prediction" element={<StudentPrediction />} />
          <Route path="semester" element={<SemesterPrediction />} />
          <Route path="attendance" element={<AttendancePrediction />} />
          <Route path="risk" element={<RiskAnalysis />} />
          <Route path="explainability" element={<Explainability />} />
          <Route path="reports" element={<Reports />} />
          <Route path="settings" element={<Settings />} />
        </Route>
      </Routes>
    </Router>
  );
}

export default App;
