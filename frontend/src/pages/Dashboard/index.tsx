import React from 'react';
import { Users, AlertTriangle, BookOpen, TrendingUp } from 'lucide-react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, LineChart, Line } from 'recharts';

const barData = [
  { name: 'Week 1', attendance: 95 },
  { name: 'Week 2', attendance: 92 },
  { name: 'Week 3', attendance: 88 },
  { name: 'Week 4', attendance: 85 },
];

const lineData = [
  { name: 'Jan', risk: 10 },
  { name: 'Feb', risk: 15 },
  { name: 'Mar', risk: 12 },
  { name: 'Apr', risk: 18 },
];

export default function Dashboard() {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-6">Dashboard</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
        <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-100 flex items-center space-x-4">
          <div className="p-3 bg-blue-100 text-blue-600 rounded-full"><Users size={24} /></div>
          <div><p className="text-sm text-gray-500">Total Students</p><p className="text-2xl font-semibold">1,245</p></div>
        </div>
        <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-100 flex items-center space-x-4">
          <div className="p-3 bg-red-100 text-red-600 rounded-full"><AlertTriangle size={24} /></div>
          <div><p className="text-sm text-gray-500">High Risk</p><p className="text-2xl font-semibold">124</p></div>
        </div>
        <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-100 flex items-center space-x-4">
          <div className="p-3 bg-green-100 text-green-600 rounded-full"><BookOpen size={24} /></div>
          <div><p className="text-sm text-gray-500">Avg Attendance</p><p className="text-2xl font-semibold">89%</p></div>
        </div>
        <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-100 flex items-center space-x-4">
          <div className="p-3 bg-purple-100 text-purple-600 rounded-full"><TrendingUp size={24} /></div>
          <div><p className="text-sm text-gray-500">Model Accuracy</p><p className="text-2xl font-semibold">94.2%</p></div>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-100">
          <h2 className="text-lg font-semibold mb-4">Attendance Trends</h2>
          <div className="h-64">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={barData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" />
                <YAxis />
                <Tooltip />
                <Bar dataKey="attendance" fill="#3b82f6" />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
        <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-100">
          <h2 className="text-lg font-semibold mb-4">Risk Level Over Time</h2>
          <div className="h-64">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={lineData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" />
                <YAxis />
                <Tooltip />
                <Line type="monotone" dataKey="risk" stroke="#ef4444" strokeWidth={2} />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>
    </div>
  );
}
