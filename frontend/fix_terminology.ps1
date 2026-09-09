$explain = Get-Content "src/pages/Explainability/index.tsx" -Raw
$explain = $explain -replace "Prior Grades", "Prior SGPA"
Set-Content "src/pages/Explainability/index.tsx" -Value $explain

$dataset = Get-Content "src/pages/DatasetManagement/index.tsx" -Raw
$dataset = $dataset -replace "historical_grades_2023.csv", "btech_results_2023.csv"
Set-Content "src/pages/DatasetManagement/index.tsx" -Value $dataset

$training = Get-Content "src/pages/ModelTraining/index.tsx" -Raw
$training = $training -replace "Final Grade", "Final CGPA"
$training = $training -replace "historical_grades_2023.csv", "btech_results_2023.csv"
Set-Content "src/pages/ModelTraining/index.tsx" -Value $training

$risk = Get-Content "src/pages/RiskAnalysis/index.tsx" -Raw
$risk = $risk -replace "Class 10", "3rd Sem"
$risk = $risk -replace "Class 11", "5th Sem"
$risk = $risk -replace "Class 9", "1st Sem"
$risk = $risk -replace "Class 12", "7th Sem"
$risk = $risk -replace ">Grade<", ">Semester<"
Set-Content "src/pages/RiskAnalysis/index.tsx" -Value $risk

# Also search for 'School' just in case
$app = Get-ChildItem -Path "src\pages" -Recurse -Filter "*.tsx" | ForEach-Object {
    $content = Get-Content $_.FullName -Raw
    if ($content -match "School") {
        $content = $content -replace "School", "College"
        Set-Content $_.FullName -Value $content
    }
}
