$baseDir = "C:\Users\Hi\.gemini\antigravity\scratch\edupredict-frontend"

# 1. Update StudentPrediction for B.Tech
$btechRisk = @"
import React, { useState } from 'react';
import { useForm } from 'react-hook-form';
import { AlertCircle, User, Target } from 'lucide-react';

type FormData = {
  rollNo: string;
  branch: string;
  semester: string;
  cgpa: number;
  activeBacklogs: number;
  attendance: number;
};

export default function StudentPrediction() {
  const { register, handleSubmit } = useForm<FormData>();
  const [prediction, setPrediction] = useState<{ risk: string, probability: number } | null>(null);

  const onSubmit = (data: FormData) => {
    // Mock logic for B.Tech risk (Risk of year-back or dropout)
    const score = (data.cgpa * 10) * 0.4 + data.attendance * 0.4 - (data.activeBacklogs * 10);
    const probability = Math.max(0, Math.min(100, 100 - score + 20)); 
    let risk = 'Low';
    if (probability > 70) risk = 'High';
    else if (probability > 40) risk = 'Medium';

    setPrediction({ risk, probability: Math.round(probability) });
  };

  return (
    <div className="p-6 max-w-4xl mx-auto">
      <h1 className="text-2xl font-bold mb-6 text-gray-800">B.Tech Student Risk Prediction</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
          <h2 className="text-lg font-semibold mb-4 border-b pb-2">Student Data</h2>
          <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
            <div>
              <label className="block text-sm font-medium text-gray-700">University Roll No</label>
              <input type="text" {...register('rollNo')} required className="mt-1 focus:ring-blue-500 focus:border-blue-500 block w-full sm:text-sm border-gray-300 rounded-md py-2 px-3 border" placeholder="e.g. 21CS001" />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700">Engineering Branch</label>
              <select {...register('branch')} className="mt-1 block w-full py-2 px-3 border border-gray-300 rounded-md sm:text-sm">
                <option value="CSE">Computer Science (CSE)</option>
                <option value="ECE">Electronics (ECE)</option>
                <option value="ME">Mechanical (ME)</option>
                <option value="CE">Civil (CE)</option>
                <option value="IT">Information Tech (IT)</option>
              </select>
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700">Current Semester</label>
              <select {...register('semester')} className="mt-1 block w-full py-2 px-3 border border-gray-300 rounded-md sm:text-sm">
                <option value="1">1st Sem</option>
                <option value="2">2nd Sem</option>
                <option value="3">3rd Sem</option>
                <option value="4">4th Sem</option>
                <option value="5">5th Sem</option>
                <option value="6">6th Sem</option>
                <option value="7">7th Sem</option>
                <option value="8">8th Sem</option>
              </select>
            </div>
            
            <div>
              <label className="block text-sm font-medium text-gray-700">Current CGPA (0-10)</label>
              <input type="number" step="0.01" {...register('cgpa')} required className="mt-1 focus:ring-blue-500 focus:border-blue-500 block w-full sm:text-sm border-gray-300 rounded-md py-2 px-3 border" placeholder="7.5" />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700">Active Backlogs</label>
              <input type="number" {...register('activeBacklogs')} required className="mt-1 focus:ring-blue-500 focus:border-blue-500 block w-full sm:text-sm border-gray-300 rounded-md py-2 px-3 border" placeholder="0" />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700">Overall Attendance (%)</label>
              <input type="number" {...register('attendance')} required className="mt-1 focus:ring-blue-500 focus:border-blue-500 block w-full sm:text-sm border-gray-300 rounded-md py-2 px-3 border" placeholder="85" />
            </div>

            <button type="submit" className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700">
              Run Risk Prediction
            </button>
          </form>
        </div>

        <div>
          {prediction ? (
            <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-200 h-full flex flex-col justify-center items-center text-center">
              <AlertCircle size={48} className={prediction.risk === 'High' ? 'text-red-500' : prediction.risk === 'Medium' ? 'text-yellow-500' : 'text-green-500'} />
              <h2 className="mt-4 text-2xl font-bold text-gray-900">Risk Level: {prediction.risk}</h2>
              <p className="mt-2 text-gray-600">Year-Back / Dropout Probability</p>
              <div className="mt-2 text-4xl font-extrabold text-gray-800">{prediction.probability}%</div>
              
              <div className="mt-6 w-full bg-gray-200 rounded-full h-2.5">
                <div className={`h-2.5 rounded-full ${prediction.risk === 'High' ? 'bg-red-500' : prediction.risk === 'Medium' ? 'bg-yellow-500' : 'bg-green-500'}`} style={{ width: `${prediction.probability}%` }}></div>
              </div>
            </div>
          ) : (
            <div className="bg-gray-50 p-6 rounded-lg border border-dashed border-gray-300 h-full flex flex-col justify-center items-center text-gray-400">
              <Target size={48} className="mb-4 text-gray-300" />
              <p>Enter B.Tech student details to predict academic risk.</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
"@
Set-Content -Path "$baseDir\src\pages\StudentPrediction\index.tsx" -Value $btechRisk

# 2. Update Layout.tsx with new routes
$layoutContent = Get-Content "$baseDir\src\components\common\Layout.tsx" -Raw
$layoutContent = $layoutContent -replace "import { LayoutDashboard", "import { LayoutDashboard, Calendar, BookOpen"
$layoutContent = $layoutContent -replace "  \{ name: 'Prediction', path: '/prediction', icon: UserCheck \},", "  { name: 'Risk Prediction', path: '/prediction', icon: UserCheck },
  { name: 'Sem Prediction', path: '/semester', icon: BookOpen },
  { name: 'Attendance Pred', path: '/attendance', icon: Calendar },"
Set-Content -Path "$baseDir\src\components\common\Layout.tsx" -Value $layoutContent

# 3. Update App.tsx with new routes
$appContent = Get-Content "$baseDir\src\App.tsx" -Raw
$appContent = $appContent -replace "import StudentPrediction", "import StudentPrediction from './pages/StudentPrediction';`nimport SemesterPrediction from './pages/SemesterPrediction';`nimport AttendancePrediction from './pages/AttendancePrediction';"
$appContent = $appContent -replace "<Route path=`"prediction`" element=\{<StudentPrediction />\} />", "<Route path=`"prediction`" element={<StudentPrediction />} />`n          <Route path=`"semester`" element={<SemesterPrediction />} />`n          <Route path=`"attendance`" element={<AttendancePrediction />} />"
Set-Content -Path "$baseDir\src\App.tsx" -Value $appContent
