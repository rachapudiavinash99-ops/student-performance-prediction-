$baseDir = "C:\Users\Hi\.gemini\antigravity\scratch\Student Performance Prediction-frontend"

# src/main.tsx
$main = @"
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
"@
Set-Content -Path "$baseDir\src\main.tsx" -Value $main

# src/App.tsx
$app = @"
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Layout from './components/common/Layout';
import Dashboard from './pages/Dashboard';
import DatasetManagement from './pages/DatasetManagement';
import ModelTraining from './pages/ModelTraining';
import ModelComparison from './pages/ModelComparison';
import StudentPrediction from './pages/StudentPrediction';
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
"@
Set-Content -Path "$baseDir\src\App.tsx" -Value $app

# Layout Component
$layout = @"
import { Outlet, Link, useLocation } from 'react-router-dom';
import { LayoutDashboard, Database, Brain, BarChart2, UserCheck, AlertTriangle, Lightbulb, FileText, Settings, LogOut, Search, Bell, User } from 'lucide-react';

const navItems = [
  { name: 'Dashboard', path: '/dashboard', icon: LayoutDashboard },
  { name: 'Datasets', path: '/datasets', icon: Database },
  { name: 'Model Training', path: '/training', icon: Brain },
  { name: 'Comparison', path: '/comparison', icon: BarChart2 },
  { name: 'Prediction', path: '/prediction', icon: UserCheck },
  { name: 'Risk Analysis', path: '/risk', icon: AlertTriangle },
  { name: 'Explainability', path: '/explainability', icon: Lightbulb },
  { name: 'Reports', path: '/reports', icon: FileText },
  { name: 'Settings', path: '/settings', icon: Settings },
];

export default function Layout() {
  const location = useLocation();

  return (
    <div className="flex h-screen bg-gray-50 dark:bg-gray-900">
      {/* Sidebar */}
      <aside className="w-64 bg-white dark:bg-gray-800 border-r border-gray-200 dark:border-gray-700 flex flex-col">
        <div className="h-16 flex items-center px-6 border-b border-gray-200 dark:border-gray-700">
          <Brain className="w-8 h-8 text-blue-600 mr-2" />
          <span className="text-xl font-bold text-gray-900 dark:text-white">Student Performance Prediction</span>
        </div>
        <nav className="flex-1 overflow-y-auto py-4">
          <ul className="space-y-1 px-3">
            {navItems.map((item) => {
              const Icon = item.icon;
              const isActive = location.pathname.startsWith(item.path);
              return (
                <li key={item.name}>
                  <Link
                    to={item.path}
                    className={`flex items-center px-3 py-2 rounded-md text-sm font-medium transition-colors ` + (isActive ? 'bg-blue-50 text-blue-700 dark:bg-blue-900/50 dark:text-blue-200' : 'text-gray-700 hover:bg-gray-100 dark:text-gray-300 dark:hover:bg-gray-700')}
                  >
                    <Icon className={`mr-3 h-5 w-5 ` + (isActive ? 'text-blue-700 dark:text-blue-200' : 'text-gray-400 dark:text-gray-500')} />
                    {item.name}
                  </Link>
                </li>
              );
            })}
          </ul>
        </nav>
        <div className="p-4 border-t border-gray-200 dark:border-gray-700">
          <Link to="/login" className="flex items-center px-3 py-2 text-sm font-medium text-gray-700 hover:bg-gray-100 rounded-md dark:text-gray-300 dark:hover:bg-gray-700">
            <LogOut className="mr-3 h-5 w-5 text-gray-400" />
            Logout
          </Link>
        </div>
      </aside>

      {/* Main content */}
      <div className="flex-1 flex flex-col overflow-hidden">
        {/* Top bar */}
        <header className="h-16 bg-white dark:bg-gray-800 border-b border-gray-200 dark:border-gray-700 flex items-center justify-between px-6">
          <h1 className="text-xl font-semibold text-gray-900 dark:text-white capitalize">
            {location.pathname.split('/')[1] || 'Dashboard'}
          </h1>
          <div className="flex items-center space-x-4">
            <div className="relative">
              <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-gray-400" />
              <input type="text" placeholder="Search..." className="pl-10 pr-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md text-sm bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-blue-500" />
            </div>
            <button className="text-gray-400 hover:text-gray-500 dark:hover:text-gray-300">
              <Bell className="h-6 w-6" />
            </button>
            <button className="bg-gray-100 dark:bg-gray-700 p-2 rounded-full">
              <User className="h-5 w-5 text-gray-600 dark:text-gray-300" />
            </button>
          </div>
        </header>

        {/* Page content */}
        <main className="flex-1 overflow-y-auto p-6 bg-gray-50 dark:bg-gray-900">
          <Outlet />
        </main>
      </div>
    </div>
  );
}
"@
Set-Content -Path "$baseDir\src\components\common\Layout.tsx" -Value $layout

# Pages Mock
$pages = @("Dashboard", "DatasetManagement", "ModelTraining", "ModelComparison", "StudentPrediction", "RiskAnalysis", "Explainability", "Reports", "Settings", "Login")

foreach ($page in $pages) {
  $content = @"
export default function $page() {
  return (
    <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
      <h2 className="text-lg font-medium text-gray-900 dark:text-white mb-4">$page</h2>
      <p className="text-gray-500 dark:text-gray-400">Content for $page goes here.</p>
    </div>
  );
}
"@
  Set-Content -Path "$baseDir\src\pages\$page\index.tsx" -Value $content
}
