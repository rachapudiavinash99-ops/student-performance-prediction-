$baseDir = "C:\Users\Hi\.gemini\antigravity\scratch\edupredict-frontend"

# Create Directories
New-Item -ItemType Directory -Force -Path "$baseDir\src\pages\AttendancePrediction"
New-Item -ItemType Directory -Force -Path "$baseDir\src\pages\SemesterPrediction"

# Attendance Prediction Page
$attendanceContent = @"
import React, { useState } from 'react';
import { useForm } from 'react-hook-form';
import { Calendar, User, Target } from 'lucide-react';

type FormData = { studentId: string; previousAttendance: number; healthStatus: string; distance: number; };

export default function AttendancePrediction() {
  const { register, handleSubmit } = useForm<FormData>();
  const [prediction, setPrediction] = useState<{ attendance: number } | null>(null);

  const onSubmit = (data: FormData) => {
    // Mock logic
    const score = data.previousAttendance * 0.7 - (data.distance * 0.5) + (data.healthStatus === 'Good' ? 10 : 0);
    const prob = Math.max(0, Math.min(100, score));
    setPrediction({ attendance: Math.round(prob) });
  };

  return (
    <div className="p-6 max-w-4xl mx-auto">
      <h1 className="text-2xl font-bold mb-6 text-gray-800">Attendance Prediction</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
          <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
            <div>
              <label className="block text-sm font-medium text-gray-700">Roll No</label>
              <input type="text" {...register('studentId')} required className="mt-1 block w-full border-gray-300 rounded-md py-2 px-3 border" placeholder="e.g. 1024501" />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700">Previous Sem Attendance (%)</label>
              <input type="number" {...register('previousAttendance')} required className="mt-1 block w-full border-gray-300 rounded-md py-2 px-3 border" />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700">Health Status</label>
              <select {...register('healthStatus')} className="mt-1 block w-full border-gray-300 rounded-md py-2 px-3 border">
                <option value="Good">Good</option>
                <option value="Average">Average</option>
                <option value="Poor">Poor</option>
              </select>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700">Distance from College (km)</label>
              <input type="number" {...register('distance')} required className="mt-1 block w-full border-gray-300 rounded-md py-2 px-3 border" />
            </div>
            <button type="submit" className="w-full py-2 px-4 bg-blue-600 text-white rounded-md">Predict Attendance</button>
          </form>
        </div>
        <div>
          {prediction ? (
            <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-200 text-center h-full flex flex-col justify-center items-center">
              <Calendar size={48} className="text-blue-500 mb-4" />
              <h2 className="text-2xl font-bold text-gray-900">Predicted Attendance</h2>
              <div className="mt-2 text-5xl font-extrabold text-blue-600">{prediction.attendance}%</div>
            </div>
          ) : (
            <div className="bg-gray-50 p-6 rounded-lg border border-dashed border-gray-300 h-full flex flex-col justify-center items-center text-gray-400">
              <Target size={48} className="mb-4" />
              <p>Enter details to predict attendance.</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
"@
Set-Content -Path "$baseDir\src\pages\AttendancePrediction\index.tsx" -Value $attendanceContent

# Semester Prediction Page
$semContent = @"
import React, { useState } from 'react';
import { useForm } from 'react-hook-form';
import { BookOpen, Target } from 'lucide-react';

type FormData = { studentId: string; midSemMarks: number; attendance: number; assignments: number; };

export default function SemesterPrediction() {
  const { register, handleSubmit } = useForm<FormData>();
  const [prediction, setPrediction] = useState<{ grade: string, sgpa: number } | null>(null);

  const onSubmit = (data: FormData) => {
    // Mock logic
    const score = (data.midSemMarks * 0.4) + (data.attendance * 0.4) + (data.assignments * 2);
    let grade = 'C';
    let sgpa = 6.5;
    if (score > 85) { grade = 'O'; sgpa = 9.5; }
    else if (score > 75) { grade = 'A+'; sgpa = 8.5; }
    else if (score > 65) { grade = 'A'; sgpa = 7.5; }
    else if (score > 55) { grade = 'B+'; sgpa = 6.5; }
    else { grade = 'F'; sgpa = 4.0; }
    
    setPrediction({ grade, sgpa });
  };

  return (
    <div className="p-6 max-w-4xl mx-auto">
      <h1 className="text-2xl font-bold mb-6 text-gray-800">Semester Performance Prediction</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
          <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
            <div>
              <label className="block text-sm font-medium text-gray-700">Roll No</label>
              <input type="text" {...register('studentId')} required className="mt-1 block w-full border-gray-300 rounded-md py-2 px-3 border" />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700">Mid-Sem Marks (%)</label>
              <input type="number" {...register('midSemMarks')} required className="mt-1 block w-full border-gray-300 rounded-md py-2 px-3 border" />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700">Current Attendance (%)</label>
              <input type="number" {...register('attendance')} required className="mt-1 block w-full border-gray-300 rounded-md py-2 px-3 border" />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700">Assignments Completed (out of 10)</label>
              <input type="number" {...register('assignments')} required className="mt-1 block w-full border-gray-300 rounded-md py-2 px-3 border" />
            </div>
            <button type="submit" className="w-full py-2 px-4 bg-purple-600 text-white rounded-md">Predict Sem Marks</button>
          </form>
        </div>
        <div>
          {prediction ? (
            <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-200 text-center h-full flex flex-col justify-center items-center">
              <BookOpen size={48} className="text-purple-500 mb-4" />
              <h2 className="text-2xl font-bold text-gray-900">Predicted Grade: {prediction.grade}</h2>
              <p className="mt-2 text-gray-600">Expected SGPA</p>
              <div className="mt-2 text-5xl font-extrabold text-purple-600">{prediction.sgpa}</div>
            </div>
          ) : (
            <div className="bg-gray-50 p-6 rounded-lg border border-dashed border-gray-300 h-full flex flex-col justify-center items-center text-gray-400">
              <Target size={48} className="mb-4" />
              <p>Enter details to predict end semester performance.</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
"@
Set-Content -Path "$baseDir\src\pages\SemesterPrediction\index.tsx" -Value $semContent
