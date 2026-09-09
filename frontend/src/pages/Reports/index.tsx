import React from 'react';
import { FileDown, FileText, Calendar } from 'lucide-react';

const reports = [
  { id: 1, title: 'Q3 College-wide Risk Summary', date: '2023-10-01', type: 'PDF' },
  { id: 2, title: 'Department Comparison Analysis', date: '2023-09-15', type: 'Excel' },
  { id: 3, title: 'High-Risk Intervention Outcomes', date: '2023-09-01', type: 'PDF' },
  { id: 4, title: 'Monthly Attendance Forecasting', date: '2023-08-30', type: 'CSV' },
];

export default function Reports() {
  return (
    <div className="p-6 max-w-4xl mx-auto">
      <h1 className="text-2xl font-bold mb-6 text-gray-800">Generated Reports</h1>
      
      <div className="grid grid-cols-1 gap-4">
        {reports.map(report => (
          <div key={report.id} className="bg-white p-5 rounded-lg shadow-sm border border-gray-200 flex items-center justify-between hover:shadow-md transition-shadow">
            <div className="flex items-center space-x-4">
              <div className={`p-3 rounded-lg ${report.type === 'PDF' ? 'bg-red-100 text-red-600' : report.type === 'Excel' ? 'bg-green-100 text-green-600' : 'bg-gray-100 text-gray-600'}`}>
                <FileText size={24} />
              </div>
              <div>
                <h3 className="text-lg font-medium text-gray-900">{report.title}</h3>
                <div className="flex items-center text-sm text-gray-500 mt-1">
                  <Calendar size={14} className="mr-1" /> {report.date} • {report.type}
                </div>
              </div>
            </div>
            
            <button className="flex items-center px-4 py-2 border border-gray-300 rounded-md text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">
              <FileDown size={16} className="mr-2" /> Download
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}

