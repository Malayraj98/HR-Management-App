from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime, timedelta
import random

app = Flask(__name__)
CORS(app)

# Professional data models and sample data
class ProfessionalData:
    def __init__(self):
        self.employees = self._generate_employees()
        self.performance_reviews = self._generate_performance_reviews()
        self.leave_requests = self._generate_leave_requests()
        self.payroll_records = self._generate_payroll_records()
        self.training_programs = self._generate_training_programs()
        self.candidates = self._generate_candidates()
        self.company_metrics = self._generate_company_metrics()

    def _generate_employees(self):
        return [
            {
                "id": 1,
                "name": "Sarah Chen",
                "department": "Engineering",
                "position": "Senior Software Engineer",
                "hire_date": "2021-03-15",
                "performance_score": 4.7,
                "salary": 125000,
                "email": "sarah.chen@company.com",
                "avatar": "/api/avatars/1",
                "location": "San Francisco, CA",
                "status": "Active"
            },
            {
                "id": 2,
                "name": "Marcus Johnson",
                "department": "Marketing",
                "position": "Marketing Director",
                "hire_date": "2019-07-22",
                "performance_score": 4.5,
                "salary": 110000,
                "email": "marcus.johnson@company.com",
                "avatar": "/api/avatars/2",
                "location": "New York, NY",
                "status": "Active"
            },
            {
                "id": 3,
                "name": "Elena Rodriguez",
                "department": "Sales",
                "position": "Account Executive",
                "hire_date": "2022-01-10",
                "performance_score": 4.2,
                "salary": 85000,
                "email": "elena.rodriguez@company.com",
                "avatar": "/api/avatars/3",
                "location": "Austin, TX",
                "status": "Active"
            },
            {
                "id": 4,
                "name": "David Kim",
                "department": "HR",
                "position": "HR Business Partner",
                "hire_date": "2020-11-05",
                "performance_score": 4.8,
                "salary": 95000,
                "email": "david.kim@company.com",
                "avatar": "/api/avatars/4",
                "location": "Chicago, IL",
                "status": "Active"
            },
            {
                "id": 5,
                "name": "Priya Patel",
                "department": "Engineering",
                "position": "DevOps Engineer",
                "hire_date": "2023-05-30",
                "performance_score": 4.3,
                "salary": 115000,
                "email": "priya.patel@company.com",
                "avatar": "/api/avatars/5",
                "location": "Remote",
                "status": "Active"
            }
        ]

    def _generate_performance_reviews(self):
        return [
            {
                "id": 1,
                "employee_id": 1,
                "review_date": "2024-01-15",
                "reviewer": "Tech Lead Manager",
                "goals_achievement": 4.5,
                "teamwork": 4.8,
                "innovation": 4.7,
                "communication": 4.3,
                "overall_score": 4.6,
                "feedback": "Exceptional technical contributions and strong leadership in the recent project launch. Consistently exceeds expectations.",
                "goals": "Lead architecture redesign, mentor junior engineers, improve system performance by 15%",
                "status": "Completed"
            },
            {
                "id": 2,
                "employee_id": 2,
                "review_date": "2024-01-10",
                "reviewer": "VP of Marketing",
                "goals_achievement": 4.2,
                "teamwork": 4.5,
                "innovation": 4.8,
                "communication": 4.7,
                "overall_score": 4.6,
                "feedback": "Outstanding campaign results with 40% increase in lead generation. Strong cross-functional collaboration.",
                "goals": "Increase brand awareness, launch new product campaign, improve marketing ROI",
                "status": "Completed"
            }
        ]

    def _generate_leave_requests(self):
        return [
            {
                "id": 1,
                "employee_id": 1,
                "employee_name": "Sarah Chen",
                "leave_type": "Vacation",
                "start_date": "2024-02-01",
                "end_date": "2024-02-05",
                "status": "Approved",
                "reason": "Family vacation",
                "days_requested": 5,
                "submitted_date": "2024-01-15"
            },
            {
                "id": 2,
                "employee_id": 3,
                "employee_name": "Elena Rodriguez",
                "leave_type": "Sick Leave",
                "start_date": "2024-01-20",
                "end_date": "2024-01-21",
                "status": "Approved",
                "reason": "Medical appointment",
                "days_requested": 2,
                "submitted_date": "2024-01-18"
            },
            {
                "id": 3,
                "employee_id": 2,
                "employee_name": "Marcus Johnson",
                "leave_type": "Vacation",
                "start_date": "2024-03-01",
                "end_date": "2024-03-10",
                "status": "Pending",
                "reason": "International travel for team offsite",
                "days_requested": 8,
                "submitted_date": "2024-01-20"
            }
        ]

    def _generate_payroll_records(self):
        return [
            {
                "id": 1,
                "employee_id": 1,
                "employee_name": "Sarah Chen",
                "pay_period": "2024-01",
                "basic_salary": 10416.67,
                "bonus": 2000,
                "overtime": 1500,
                "deductions": 1800,
                "net_salary": 12116.67,
                "taxes": 3200,
                "benefits": 800,
                "status": "Processed"
            },
            {
                "id": 2,
                "employee_id": 2,
                "employee_name": "Marcus Johnson",
                "pay_period": "2024-01",
                "basic_salary": 9166.67,
                "bonus": 1500,
                "overtime": 800,
                "deductions": 1600,
                "net_salary": 9866.67,
                "taxes": 2800,
                "benefits": 700,
                "status": "Processed"
            }
        ]

    def _generate_training_programs(self):
        return [
            {
                "id": 1,
                "title": "Leadership Development Program",
                "description": "Advanced leadership skills and strategic thinking for senior managers and directors.",
                "duration": "8 weeks",
                "instructor": "Dr. James Wilson",
                "enrolled_employees": [1, 2],
                "max_capacity": 15,
                "start_date": "2024-02-15",
                "end_date": "2024-04-15",
                "status": "Upcoming",
                "category": "Leadership"
            },
            {
                "id": 2,
                "title": "AI & Machine Learning Fundamentals",
                "description": "Comprehensive introduction to AI and ML technologies for technical teams.",
                "duration": "6 weeks",
                "instructor": "Prof. Sarah Chen",
                "enrolled_employees": [3, 5],
                "max_capacity": 20,
                "start_date": "2024-03-01",
                "end_date": "2024-04-15",
                "status": "Upcoming",
                "category": "Technical"
            }
        ]

    def _generate_candidates(self):
        return [
            {
                "id": 1,
                "name": "Jennifer Lee",
                "applied_position": "Frontend Developer",
                "experience": "5 years",
                "status": "Technical Interview",
                "ai_match_score": 92,
                "applied_date": "2024-01-15",
                "current_stage": 3,
                "total_stages": 4,
                "skills": ["React", "TypeScript", "Node.js"],
                "location": "San Francisco, CA"
            }
        ]

    def _generate_company_metrics(self):
        return {
            "total_employees": 1247,
            "open_positions": 8,
            "employee_engagement": 87,
            "avg_tenure": 2.8,
            "diversity_index": 76,
            "retention_rate": 94,
            "avg_time_to_hire": 32,
            "training_completion": 82
        }

# Initialize data
data = ProfessionalData()

# AI Analytics Engine
class AIAnalyticsEngine:
    def __init__(self, data):
        self.data = data

    def predict_employee_churn(self, employee):
        """Advanced churn prediction using multiple factors"""
        tenure = (datetime.now() - datetime.strptime(employee['hire_date'], '%Y-%m-%d')).days / 365.25
        performance = employee['performance_score']
        
        # Advanced algorithm considering multiple factors
        churn_score = max(0, min(100,
            (5 - performance) * 12 +  # Performance impact
            max(0, tenure - 1.5) * 10 +  # Tenure impact (highest risk at 1.5-3 years)
            random.randint(-8, 8)  # Random factor
        ))
        
        return {
            "employee_id": employee['id'],
            "employee_name": employee['name'],
            "churn_probability": round(churn_score),
            "risk_level": "High" if churn_score > 70 else "Medium" if churn_score > 40 else "Low",
            "key_factors": self._identify_churn_factors(employee, churn_score),
            "recommended_actions": self._generate_retention_actions(employee, churn_score)
        }

    def _identify_churn_factors(self, employee, churn_score):
        factors = []
        if employee['performance_score'] < 4.0:
            factors.append("Performance concerns")
        if churn_score > 60:
            factors.append("Career growth opportunities")
        if random.random() > 0.7:
            factors.append("Work-life balance")
        return factors

    def _generate_retention_actions(self, employee, churn_score):
        actions = []
        if churn_score > 70:
            actions.extend(["Schedule retention meeting", "Review compensation", "Career path discussion"])
        elif churn_score > 50:
            actions.extend(["Check-in meeting", "Skill development plan"])
        return actions

    def generate_ai_insights(self):
        """Generate professional AI insights for dashboard"""
        insights = []
        
        # Engagement insights
        avg_engagement = sum(emp['performance_score'] for emp in self.data.employees) / len(self.data.employees)
        if avg_engagement > 4.5:
            insights.append("High overall employee engagement detected. Consider leveraging this for innovation initiatives.")
        
        # Leave pattern insights
        pending_leaves = len([lr for lr in self.data.leave_requests if lr['status'] == 'Pending'])
        if pending_leaves > 2:
            insights.append(f"{pending_leaves} pending leave requests require attention. Consider implementing automated approval workflows.")
        
        # Performance insights
        high_performers = len([emp for emp in self.data.employees if emp['performance_score'] >= 4.5])
        if high_performers / len(self.data.employees) > 0.6:
            insights.append("Exceptional performance distribution. 60% of employees are high performers.")
        
        # Training insights
        total_enrollments = sum(len(program['enrolled_employees']) for program in self.data.training_programs)
        if total_enrollments / len(self.data.employees) < 0.3:
            insights.append("Low training enrollment. Consider promoting learning culture and development opportunities.")
        
        return insights

# Initialize AI engine
ai_engine = AIAnalyticsEngine(data)

# Utility functions
def get_next_id(collection):
    return max(item['id'] for item in collection) + 1 if collection else 1

# Professional API Routes
@app.route('/')
def home():
    return jsonify({
        "message": "HR AI Pro API - Professional HR Management Platform",
        "version": "2.0",
        "status": "operational",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/health')
def health_check():
    return jsonify({
        "status": "healthy",
        "version": "2.0",
        "environment": "production",
        "timestamp": datetime.now().isoformat(),
        "features": [
            "AI-Powered Analytics",
            "Employee Management",
            "Performance Reviews",
            "Leave Management",
            "Payroll Integration",
            "Training & Development",
            "Recruitment Automation"
        ]
    })

# Employee Management Endpoints
@app.route('/api/employees', methods=['GET', 'POST'])
def handle_employees():
    if request.method == 'GET':
        department = request.args.get('department')
        status = request.args.get('status', 'Active')
        
        filtered_employees = data.employees
        
        if department:
            filtered_employees = [emp for emp in filtered_employees if emp['department'].lower() == department.lower()]
        
        if status:
            filtered_employees = [emp for emp in filtered_employees if emp['status'] == status]
        
        return jsonify({
            "employees": filtered_employees,
            "count": len(filtered_employees),
            "departments": list(set(emp['department'] for emp in data.employees)),
            "summary": {
                "total": len(filtered_employees),
                "by_department": {dept: len([emp for emp in filtered_employees if emp['department'] == dept]) 
                                for dept in set(emp['department'] for emp in filtered_employees)}
            }
        })
    
    elif request.method == 'POST':
        employee_data = request.json
        
        new_employee = {
            "id": get_next_id(data.employees),
            "name": employee_data.get('name'),
            "department": employee_data.get('department'),
            "position": employee_data.get('position'),
            "hire_date": employee_data.get('hire_date', datetime.now().strftime('%Y-%m-%d')),
            "performance_score": float(employee_data.get('performance_score', 4.0)),
            "salary": float(employee_data.get('salary', 50000)),
            "email": employee_data.get('email'),
            "avatar": f"/api/avatars/{get_next_id(data.employees)}",
            "location": employee_data.get('location', 'Remote'),
            "status": "Active"
        }
        
        data.employees.append(new_employee)
        return jsonify(new_employee), 201

# Advanced Analytics Endpoints
@app.route('/api/analytics/dashboard', methods=['GET'])
def get_dashboard_analytics():
    # Company metrics
    company_metrics = data.company_metrics
    
    # Real-time calculations
    total_employees = len(data.employees)
    open_positions = 8
    pending_leave_requests = len([lr for lr in data.leave_requests if lr['status'] == 'Pending'])
    active_training_programs = len([tp for tp in data.training_programs if tp['status'] in ['Active', 'Upcoming']])
    
    # AI-generated insights
    ai_insights = ai_engine.generate_ai_insights()
    
    # Performance metrics
    avg_performance = sum(emp['performance_score'] for emp in data.employees) / len(data.employees) if data.employees else 0
    high_performers = len([emp for emp in data.employees if emp['performance_score'] >= 4.5])
    
    return jsonify({
        "summary": {
            "total_employees": company_metrics['total_employees'],
            "open_positions": open_positions,
            "pending_leave_requests": pending_leave_requests,
            "active_training_programs": active_training_programs,
            "employee_engagement": company_metrics['employee_engagement'],
            "retention_rate": company_metrics['retention_rate'],
            "avg_performance_score": round(avg_performance, 1),
            "high_performers_count": high_performers
        },
        "ai_insights": ai_insights,
        "department_breakdown": {
            dept: len([emp for emp in data.employees if emp['department'] == dept])
            for dept in set(emp['department'] for emp in data.employees)
        },
        "key_metrics": {
            "time_to_hire": company_metrics['avg_time_to_hire'],
            "training_completion": company_metrics['training_completion'],
            "diversity_index": company_metrics['diversity_index']
        },
        "last_updated": datetime.now().isoformat()
    })

@app.route('/api/ai/advanced-analytics', methods=['GET'])
def get_advanced_analytics():
    # Churn predictions for all employees
    churn_predictions = [ai_engine.predict_employee_churn(emp) for emp in data.employees]
    
    # Training recommendations
    training_recommendations = []
    for employee in data.employees:
        recommendations = []
        if employee['performance_score'] < 4.0:
            recommendations.append("Performance Improvement Workshop")
        
        if employee['department'] == 'Engineering':
            recommendations.extend(["Cloud Technologies Certification", "Agile Leadership", "System Design"])
        elif employee['department'] == 'Sales':
            recommendations.extend(["Advanced Sales Techniques", "CRM Mastery", "Client Relations"])
        
        training_recommendations.append({
            "employee_id": employee['id'],
            "employee_name": employee['name'],
            "recommended_trainings": recommendations[:2]  # Top 2 recommendations
        })
    
    # Department analytics
    dept_analytics = {}
    for dept in set(emp['department'] for emp in data.employees):
        dept_employees = [emp for emp in data.employees if emp['department'] == dept]
        dept_analytics[dept] = {
            "employee_count": len(dept_employees),
            "avg_performance": sum(emp['performance_score'] for emp in dept_employees) / len(dept_employees),
            "avg_salary": sum(emp['salary'] for emp in dept_employees) / len(dept_employees),
            "high_performers": len([emp for emp in dept_employees if emp['performance_score'] >= 4.5])
        }
    
    # Salary analytics
    salaries = [emp['salary'] for emp in data.employees]
    salary_analytics = {
        "avg_salary": sum(salaries) / len(salaries),
        "max_salary": max(salaries),
        "min_salary": min(salaries),
        "salary_equity_score": round((min(salaries) / max(salaries)) * 100, 1),
        "salary_bands": {
            "entry_level": len([s for s in salaries if s < 70000]),
            "mid_level": len([s for s in salaries if 70000 <= s < 120000]),
            "senior_level": len([s for s in salaries if s >= 120000])
        }
    }
    
    return jsonify({
        "churn_predictions": churn_predictions,
        "training_recommendations": training_recommendations,
        "department_analytics": dept_analytics,
        "salary_analytics": salary_analytics,
        "workforce_trends": {
            "growth_rate": "+5.2% this quarter",
            "attrition_rate": "8.3% annual",
            "diversity_improvement": "+12% YoY"
        },
        "generated_at": datetime.now().isoformat()
    })

# Professional Workforce Planning
@app.route('/api/analytics/workforce-planning', methods=['GET'])
def workforce_planning():
    """Advanced workforce planning analytics"""
    return jsonify({
        "headcount_forecast": {
            "next_quarter": 1350,
            "next_year": 1500,
            "growth_rate": "12%"
        },
        "skill_gap_analysis": {
            "critical_skills": ["AI/ML", "Cloud Architecture", "Data Science"],
            "gap_severity": "High",
            "recommended_hires": 15
        },
        "succession_planning": {
            "key_positions_at_risk": 3,
            "ready_now_candidates": 8,
            "development_plans_needed": 12
        }
    })

# Compliance and Audit
@app.route('/api/compliance/audit', methods=['GET'])
def compliance_audit():
    """Compliance and audit tracking"""
    return jsonify({
        "pending_compliance_issues": 5,
        "upcoming_deadlines": [
            {"type": "EEO Reporting", "deadline": "2024-03-31", "status": "Pending"},
            {"type": "Payroll Tax", "deadline": "2024-04-15", "status": "In Progress"}
        ],
        "compliance_score": 92,
        "risk_level": "Low"
    })

# Employee Engagement
@app.route('/api/employees/engagement', methods=['GET'])
def employee_engagement():
    """Employee engagement and sentiment analysis"""
    return jsonify({
        "engagement_score": 87,
        "sentiment_trend": "Improving",
        "key_drivers": ["Career Growth", "Work-Life Balance", "Leadership"],
        "action_items": [
            "Implement flexible work arrangements",
            "Enhance career development programs",
            "Improve manager training"
        ]
    })

# Recruitment Pipeline
@app.route('/api/recruitment/pipeline', methods=['GET'])
def recruitment_pipeline():
    """Advanced recruitment pipeline analytics"""
    return jsonify({
        "pipeline_health": "Strong",
        "time_to_fill": 32,
        "candidate_conversion_rate": 28,
        "diversity_metrics": {
            "gender_ratio": {"male": 52, "female": 45, "other": 3},
            "ethnicity_breakdown": {"white": 48, "asian": 25, "black": 15, "hispanic": 12}
        },
        "cost_per_hire": 8500
    })

# Performance Management Endpoints
@app.route('/api/performance-reviews', methods=['GET', 'POST'])
def handle_performance_reviews():
    if request.method == 'GET':
        employee_id = request.args.get('employee_id')
        status = request.args.get('status')
        
        filtered_reviews = data.performance_reviews
        
        if employee_id:
            filtered_reviews = [review for review in filtered_reviews if review['employee_id'] == int(employee_id)]
        
        if status:
            filtered_reviews = [review for review in filtered_reviews if review['status'] == status]
        
        return jsonify({
            "reviews": filtered_reviews,
            "count": len(filtered_reviews),
            "summary": {
                "average_score": sum(review['overall_score'] for review in filtered_reviews) / len(filtered_reviews) if filtered_reviews else 0,
                "completed_this_quarter": len([r for r in filtered_reviews if r['status'] == 'Completed'])
            }
        })
    
    elif request.method == 'POST':
        review_data = request.json
        
        new_review = {
            "id": get_next_id(data.performance_reviews),
            "employee_id": review_data.get('employee_id'),
            "review_date": review_data.get('review_date', datetime.now().strftime('%Y-%m-%d')),
            "reviewer": review_data.get('reviewer'),
            "goals_achievement": float(review_data.get('goals_achievement', 0)),
            "teamwork": float(review_data.get('teamwork', 0)),
            "innovation": float(review_data.get('innovation', 0)),
            "communication": float(review_data.get('communication', 0)),
            "overall_score": float(review_data.get('overall_score', 0)),
            "feedback": review_data.get('feedback', ''),
            "goals": review_data.get('goals', ''),
            "status": "Pending"
        }
        
        data.performance_reviews.append(new_review)
        return jsonify(new_review), 201

# Leave Management Endpoints
@app.route('/api/leave-requests', methods=['GET', 'POST'])
def handle_leave_requests():
    if request.method == 'GET':
        employee_id = request.args.get('employee_id')
        status = request.args.get('status')
        
        filtered_requests = data.leave_requests
        
        if employee_id:
            filtered_requests = [lr for lr in filtered_requests if lr['employee_id'] == int(employee_id)]
        
        if status:
            filtered_requests = [lr for lr in filtered_requests if lr['status'] == status]
        
        return jsonify({
            "leave_requests": filtered_requests,
            "count": len(filtered_requests),
            "summary": {
                "pending": len([lr for lr in filtered_requests if lr['status'] == 'Pending']),
                "approved_this_month": len([lr for lr in filtered_requests if lr['status'] == 'Approved']),
                "avg_processing_time": "2.3 days"
            }
        })
    
    elif request.method == 'POST':
        leave_data = request.json
        employee = next((emp for emp in data.employees if emp['id'] == leave_data.get('employee_id')), None)
        
        if not employee:
            return jsonify({"error": "Employee not found"}), 404
        
        new_leave_request = {
            "id": get_next_id(data.leave_requests),
            "employee_id": leave_data.get('employee_id'),
            "employee_name": employee['name'],
            "leave_type": leave_data.get('leave_type'),
            "start_date": leave_data.get('start_date'),
            "end_date": leave_data.get('end_date'),
            "status": "Pending",
            "reason": leave_data.get('reason', ''),
            "days_requested": leave_data.get('days_requested', 1),
            "submitted_date": datetime.now().strftime('%Y-%m-%d')
        }
        
        data.leave_requests.append(new_leave_request)
        return jsonify(new_leave_request), 201

# Training & Development Endpoints
@app.route('/api/training', methods=['GET', 'POST'])
def handle_training():
    if request.method == 'GET':
        status = request.args.get('status')
        category = request.args.get('category')
        
        filtered_programs = data.training_programs
        
        if status:
            filtered_programs = [tp for tp in filtered_programs if tp['status'] == status]
        
        if category:
            filtered_programs = [tp for tp in filtered_programs if tp['category'] == category]
        
        return jsonify({
            "training_programs": filtered_programs,
            "count": len(filtered_programs),
            "categories": list(set(tp['category'] for tp in data.training_programs)),
            "summary": {
                "total_enrollments": sum(len(tp['enrolled_employees']) for tp in filtered_programs),
                "completion_rate": "78%",
                "upcoming_programs": len([tp for tp in filtered_programs if tp['status'] == 'Upcoming'])
            }
        })
    
    elif request.method == 'POST':
        training_data = request.json
        
        new_training = {
            "id": get_next_id(data.training_programs),
            "title": training_data.get('title'),
            "description": training_data.get('description'),
            "duration": training_data.get('duration'),
            "instructor": training_data.get('instructor'),
            "enrolled_employees": training_data.get('enrolled_employees', []),
            "max_capacity": training_data.get('max_capacity', 20),
            "start_date": training_data.get('start_date'),
            "end_date": training_data.get('end_date'),
            "status": "Upcoming",
            "category": training_data.get('category', 'Professional Development')
        }
        
        data.training_programs.append(new_training)
        return jsonify(new_training), 201

# Payroll Endpoints
@app.route('/api/payroll', methods=['GET'])
def get_payroll():
    pay_period = request.args.get('pay_period')
    employee_id = request.args.get('employee_id')
    
    filtered_records = data.payroll_records
    
    if pay_period:
        filtered_records = [pr for pr in filtered_records if pr['pay_period'] == pay_period]
    
    if employee_id:
        filtered_records = [pr for pr in filtered_records if pr['employee_id'] == int(employee_id)]
    
    total_payroll = sum(pr['net_salary'] for pr in filtered_records)
    
    return jsonify({
        "payroll_records": filtered_records,
        "count": len(filtered_records),
        "summary": {
            "total_payroll": total_payroll,
            "avg_salary": total_payroll / len(filtered_records) if filtered_records else 0,
            "pay_periods": list(set(pr['pay_period'] for pr in data.payroll_records))
        }
    })

if __name__ == '__main__':
    print("🚀 Starting HR AI Pro Professional API Server...")
    print("=" * 60)
    print("📊 Professional Features Enabled:")
    print("  • AI-Powered Analytics Engine")
    print("  • Advanced Employee Management")
    print("  • Performance & Development Tracking")
    print("  • Intelligent Leave Management")
    print("  • Comprehensive Payroll System")
    print("  • Recruitment Pipeline Management")
    print("  • Real-time Dashboard Analytics")
    print("  • Workforce Planning & Forecasting")
    print("  • Compliance & Audit Management")
    print("  • Employee Engagement Analytics")
    print("=" * 60)
    print("\n🌐 Server running on http://localhost:5000")
    print("📚 API Documentation: http://localhost:5000/")
    print("❤️  Health Check: http://localhost:5000/api/health")
    
    app.run(debug=True, host='0.0.0.0', port=5000)