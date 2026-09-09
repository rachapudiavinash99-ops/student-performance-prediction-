import React from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';
import { Lightbulb } from 'lucide-react';

const featureImportance = [
  { name: 'Attendance Rate', importance: 0.35 },
  { name: 'Prior SGPA', importance: 0.25 },
  { name: 'Assignments Missing', importance: 0.15 },
  { name: 'Disciplinary Actions', importance: 0.12 },
  { name: 'Socioeconomic Status', importance: 0.08 },
  { name: 'Extracurriculars', importance: 0.05 },
];

export default function Explainability() {
  return (
    <div className="p-6 max-w-5xl mx-auto">
      <h1 className="text-2xl font-bold mb-6 text-gray-800">Model Explainability (SHAP)</h1>
      
      <div className="bg-blue-50 border border-blue-200 rounded-lg p-4 mb-6 flex items-start">
        <Lightbulb className="text-blue-500 mt-1 mr-3 flex-shrink-0" size={20} />
        <p className="text-sm text-blue-800">
          This chart illustrates the global feature importance determined by the current active model (Random Forest). 
          Features with higher values have a stronger influence on predicting student dropout risk.
        </p>
      </div>

      <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
        <h2 className="text-lg font-semibold mb-6 text-gray-800">Global Feature Importance</h2>
        <div className="h-96">
          <ResponsiveContainer width="100%" height="100%">
            <BarChart layout="vertical" data={featureImportance} margin={{ top: 5, right: 30, left: 100, bottom: 5 }}>
              <CartesianGrid strokeDasharray="3 3" horizontal={false} />
              <XAxis type="number" />
              <YAxis dataKey="name" type="category" width={150} tick={{ fontSize: 12 }} />
              <Tooltip cursor={{ fill: '#f3f4f6' }} contentStyle={{ borderRadius: '8px' }} />
              <Bar dataKey="importance" fill="#8b5cf6" radius={[0, 4, 4, 0]} />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );
}

