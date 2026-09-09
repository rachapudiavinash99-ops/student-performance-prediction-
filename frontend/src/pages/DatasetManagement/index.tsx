import React, { useState } from 'react';
import { UploadCloud, FileText, Database, Trash2 } from 'lucide-react';

export default function DatasetManagement() {
  const [datasets] = useState([
    { id: 1, name: 'btech_results_2023.csv', size: '2.4 MB', rows: 15420, date: '2023-10-12' },
    { id: 2, name: 'attendance_logs_q1.csv', size: '1.1 MB', rows: 8400, date: '2023-11-05' },
    { id: 3, name: 'student_demographics.json', size: '0.8 MB', rows: 3200, date: '2023-11-10' },
  ]);

  return (
    <div className="p-6 max-w-6xl mx-auto">
      <h1 className="text-2xl font-bold mb-6 text-gray-800">Dataset Management</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-200 col-span-2">
          <div className="border-2 border-dashed border-gray-300 rounded-lg p-10 flex flex-col items-center justify-center bg-gray-50 hover:bg-gray-100 transition-colors cursor-pointer">
            <UploadCloud size={48} className="text-blue-500 mb-4" />
            <p className="text-lg font-medium text-gray-700">Click or drag file to this area to upload</p>
            <p className="text-sm text-gray-500 mt-2">Support for a single or bulk upload. Strictly prohibit from uploading company data or other band files.</p>
          </div>
        </div>
        
        <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
          <h2 className="text-lg font-semibold mb-4 flex items-center"><Database className="mr-2" size={20} /> Storage Stats</h2>
          <div className="space-y-4">
            <div>
              <div className="flex justify-between text-sm mb-1"><span>Total Storage</span><span>4.3 MB / 10 GB</span></div>
              <div className="w-full bg-gray-200 rounded-full h-2"><div className="bg-blue-600 h-2 rounded-full" style={{ width: '5%' }}></div></div>
            </div>
            <div>
              <div className="flex justify-between text-sm mb-1"><span>Datasets</span><span>3</span></div>
            </div>
            <div>
              <div className="flex justify-between text-sm mb-1"><span>Total Rows</span><span>27,020</span></div>
            </div>
          </div>
        </div>
      </div>

      <div className="bg-white rounded-lg shadow-sm border border-gray-200">
        <div className="px-6 py-4 border-b border-gray-200">
          <h2 className="text-lg font-semibold text-gray-800">Active Datasets</h2>
        </div>
        <ul className="divide-y divide-gray-200">
          {datasets.map(file => (
            <li key={file.id} className="p-6 flex items-center justify-between hover:bg-gray-50">
              <div className="flex items-center">
                <FileText size={24} className="text-gray-400 mr-4" />
                <div>
                  <h3 className="text-sm font-medium text-gray-900">{file.name}</h3>
                  <p className="text-xs text-gray-500">{file.size} • {file.rows.toLocaleString()} rows • Uploaded on {file.date}</p>
                </div>
              </div>
              <button className="text-red-500 hover:text-red-700 p-2"><Trash2 size={18} /></button>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

