import React, { useState } from 'react';
import { Play, Settings, RefreshCw } from 'lucide-react';

export default function ModelTraining() {
  const [isTraining, setIsTraining] = useState(false);
  const [progress, setProgress] = useState(0);

  const startTraining = () => {
    setIsTraining(true);
    setProgress(0);
    const interval = setInterval(() => {
      setProgress(p => {
        if (p >= 100) {
          clearInterval(interval);
          setIsTraining(false);
          return 100;
        }
        return p + 5;
      });
    }, 500);
  };

  return (
    <div className="p-6 max-w-4xl mx-auto">
      <h1 className="text-2xl font-bold mb-6 text-gray-800">Model Training Pipeline</h1>

      <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6 mb-6">
        <h2 className="text-lg font-semibold mb-4 flex items-center border-b pb-2"><Settings className="mr-2" size={20} /> Configuration</h2>
        
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Target Variable</label>
            <select className="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm rounded-md border">
              <option>Dropout Risk</option>
              <option>Final CGPA</option>
              <option>Attendance Rate</option>
            </select>
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Algorithm</label>
            <select className="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm rounded-md border">
              <option>Random Forest</option>
              <option>XGBoost</option>
              <option>Neural Network</option>
            </select>
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Train/Test Split</label>
            <input type="range" min="50" max="90" defaultValue="80" className="w-full mt-2" />
            <div className="text-xs text-gray-500 mt-1 flex justify-between"><span>50%</span><span>80% Train / 20% Test</span><span>90%</span></div>
          </div>
        </div>

        <div className="mt-6">
          <button 
            onClick={startTraining}
            disabled={isTraining}
            className={`flex items-center justify-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white ${isTraining ? 'bg-blue-400 cursor-not-allowed' : 'bg-blue-600 hover:bg-blue-700'} focus:outline-none`}
          >
            {isTraining ? <RefreshCw className="animate-spin mr-2" size={18} /> : <Play className="mr-2" size={18} />}
            {isTraining ? 'Training in Progress...' : 'Start Training'}
          </button>
        </div>
      </div>

      {isTraining && (
        <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
          <h3 className="text-sm font-medium text-gray-700 mb-2">Training Progress</h3>
          <div className="w-full bg-gray-200 rounded-full h-4 mb-2">
            <div className="bg-blue-600 h-4 rounded-full transition-all duration-300 ease-out" style={{ width: `${progress}%` }}></div>
          </div>
          <p className="text-xs text-right text-gray-500">{progress}% Complete</p>
          
          <div className="mt-4 bg-gray-900 rounded p-4 text-xs font-mono text-green-400 overflow-y-auto h-32">
            <p>&gt; Initializing environment...</p>
            {progress > 10 && <p>&gt; Loading dataset 'btech_results_2023.csv'...</p>}
            {progress > 30 && <p>&gt; Preprocessing features...</p>}
            {progress > 50 && <p>&gt; Training Random Forest model with n_estimators=100...</p>}
            {progress > 80 && <p>&gt; Evaluating on test set...</p>}
            {progress === 100 && <p className="text-white">&gt; Training complete! Accuracy: 0.942</p>}
          </div>
        </div>
      )}
    </div>
  );
}

