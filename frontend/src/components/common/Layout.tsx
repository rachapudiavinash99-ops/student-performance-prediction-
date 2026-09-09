import { Outlet, Link, useLocation } from 'react-router-dom';
import { LayoutDashboard, Calendar, BookOpen, Database, Brain, BarChart2, UserCheck, AlertTriangle, Lightbulb, FileText, Settings, LogOut, Search, Bell, User } from 'lucide-react';

const navItems = [
  { name: 'Dashboard', path: '/dashboard', icon: LayoutDashboard },
  { name: 'Datasets', path: '/datasets', icon: Database },
  { name: 'Model Training', path: '/training', icon: Brain },
  { name: 'Comparison', path: '/comparison', icon: BarChart2 },
  { name: 'Risk Prediction', path: '/prediction', icon: UserCheck },
  { name: 'Sem Prediction', path: '/semester', icon: BookOpen },
  { name: 'Attendance Pred', path: '/attendance', icon: Calendar },
  { name: 'Risk Analysis', path: '/risk', icon: AlertTriangle },
  { name: 'Explainability', path: '/explainability', icon: Lightbulb },
  { name: 'Reports', path: '/reports', icon: FileText },
  { name: 'Settings', path: '/settings', icon: Settings },
];

export default function Layout() {
  const location = useLocation();

  return (
    <div className="flex h-screen bg-gray-50 dark:bg-gray-900">
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
                    className={`flex items-center px-3 py-2 rounded-md text-sm font-medium transition-colors ${isActive ? 'bg-blue-50 text-blue-700 dark:bg-blue-900/50 dark:text-blue-200' : 'text-gray-700 hover:bg-gray-100 dark:text-gray-300 dark:hover:bg-gray-700'}`}
                  >
                    <Icon className={`mr-3 h-5 w-5 ${isActive ? 'text-blue-700 dark:text-blue-200' : 'text-gray-400 dark:text-gray-500'}`} />
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

      <div className="flex-1 flex flex-col overflow-hidden">
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

        <main className="flex-1 overflow-y-auto p-6 bg-gray-50 dark:bg-gray-900">
          <Outlet />
        </main>
      </div>
    </div>
  );
}

