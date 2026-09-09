import React from 'react';
import { AlertTriangle, Filter, Search } from 'lucide-react';

const students = [
  { id: '1024501', name: 'Aarav Patel', grade: '3rd Sem', attendance: '72%', risk: 'High', prob: '85%' },
  { id: '1024502', name: 'Diya Sharma', grade: '5th Sem', attendance: '88%', risk: 'Medium', prob: '45%' },
  { id: '1024503', name: 'Rohan Gupta', grade: '1st Sem', attendance: '95%', risk: 'Low', prob: '12%' },
  { id: '1024504', name: 'Ananya Singh', grade: '7th Sem', attendance: '65%', risk: 'High', prob: '92%' },
  { id: '1024505', name: 'Karan Verma', grade: '3rd Sem', attendance: '82%', risk: 'Medium', prob: '55%' },
];

export default function RiskAnalysis() {
  return (
    <div className="p-6 max-w-6xl mx-auto">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-2xl font-bold text-gray-800">At-Risk Students Analysis</h1>
        <div className="flex space-x-2">
          <div className="relative">
            <Search className="absolute left-3 top-2.5 text-gray-400" size={16} />
            <input type="text" placeholder="Search students..." className="pl-9 pr-4 py-2 border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500" />
          </div>
          <button className="flex items-center px-4 py-2 bg-white border border-gray-300 rounded-md text-sm hover:bg-gray-50">
            <Filter size={16} className="mr-2" /> Filter
          </button>
        </div>
      </div>

      <div className="bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden">
        <table className="min-w-full divide-y divide-gray-200">
          <thead className="bg-gray-50">
            <tr>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Student</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Semester</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Attendance</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Risk Level</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Dropout Probability</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Action</th>
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-gray-200">
            {students.map((student) => (
              <tr key={student.id} className="hover:bg-gray-50">
                <td className="px-6 py-4 whitespace-nowrap">
                  <div className="text-sm font-medium text-gray-900">{student.name}</div>
                  <div className="text-sm text-gray-500">{student.id}</div>
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{student.grade}</td>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{student.attendance}</td>
                <td className="px-6 py-4 whitespace-nowrap">
                  <span className={`px-2 inline-flex text-xs leading-5 font-semibold rounded-full ${
                    student.risk === 'High' ? 'bg-red-100 text-red-800' :
                    student.risk === 'Medium' ? 'bg-yellow-100 text-yellow-800' : 'bg-green-100 text-green-800'
                  }`}>
                    {student.risk}
                  </span>
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  <div className="flex items-center">
                    <span className="mr-2">{student.prob}</span>
                    <div className="w-16 bg-gray-200 rounded-full h-1.5">
                      <div className={`h-1.5 rounded-full ${student.risk === 'High' ? 'bg-red-500' : student.risk === 'Medium' ? 'bg-yellow-500' : 'bg-green-500'}`} style={{ width: student.prob }}></div>
                    </div>
                  </div>
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-blue-600 hover:text-blue-900 font-medium cursor-pointer">
                  View Profile
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

