import React from 'react';
import { Activity, CheckCircle, Clock } from 'lucide-react';

const models = [
  { id: 1, name: 'Random Forest', accuracy: '94.2%', f1Score: '0.91', trainingTime: '45s', status: 'Active' },
  { id: 2, name: 'Gradient Boosting', accuracy: '95.1%', f1Score: '0.93', trainingTime: '120s', status: 'Ready' },
  { id: 3, name: 'Logistic Regression', accuracy: '88.5%', f1Score: '0.85', trainingTime: '5s', status: 'Deprecated' },
  { id: 4, name: 'Neural Network', accuracy: '93.8%', f1Score: '0.90', trainingTime: '300s', status: 'Ready' },
];

export default function ModelComparison() {
  return (
    <div className="p-6 max-w-6xl mx-auto">
      <h1 className="text-2xl font-bold mb-6 text-gray-800">Model Comparison</h1>
      
      <div className="bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden">
        <table className="min-w-full divide-y divide-gray-200">
          <thead className="bg-gray-50">
            <tr>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Model Name</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Accuracy</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">F1 Score</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Training Time</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-gray-200">
            {models.map((model) => (
              <tr key={model.id} className="hover:bg-gray-50">
                <td className="px-6 py-4 whitespace-nowrap">
                  <div className="flex items-center">
                    <Activity className="text-blue-500 mr-2" size={18} />
                    <span className="font-medium text-gray-900">{model.name}</span>
                  </div>
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-600">{model.accuracy}</td>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-600">{model.f1Score}</td>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-600">
                  <div className="flex items-center">
                    <Clock size={14} className="mr-1 text-gray-400" />
                    {model.trainingTime}
                  </div>
                </td>
                <td className="px-6 py-4 whitespace-nowrap">
                  <span className={`px-2 inline-flex text-xs leading-5 font-semibold rounded-full ${
                    model.status === 'Active' ? 'bg-green-100 text-green-800' :
                    model.status === 'Ready' ? 'bg-blue-100 text-blue-800' : 'bg-gray-100 text-gray-800'
                  }`}>
                    {model.status}
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
