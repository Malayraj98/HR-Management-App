// Professional HR AI Pro Application
class HRApp {
    constructor() {
        this.API_BASE_URL = "http://localhost:5000/api";
        this.currentData = {
            employees: [],
            performanceReviews: [],
            leaveRequests: [],
            payrollRecords: [],
            trainingPrograms: [],
            analytics: {},
            dashboard: {}
        };
        
        this.init();
    }

    async init() {
        this.setupEventListeners();
        this.setupSmoothScrolling();
        this.setupAnimations();
        this.updateCopyrightYear();
        
        try {
            await this.loadAllData();
            this.initializeDashboard();
            this.showProfessionalNotification(
                'HR AI Pro Loaded Successfully!', 
                'Your intelligent HR management platform is ready.', 
                'success'
            );
        } catch (error) {
            console.error('Failed to load data:', error);
            this.loadDemoData();
            this.showProfessionalNotification(
                'Demo Mode Activated', 
                'Using sample data - backend not available', 
                'info'
            );
        }
    }

    setupEventListeners() {
        // Navigation
        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', (e) => this.handleNavigation(e));
        });

        // Dashboard tabs
        document.querySelectorAll('.tab-btn').forEach(tab => {
            tab.addEventListener('click', (e) => this.handleTabChange(e));
        });

        // Buttons
        document.querySelectorAll('.btn-primary').forEach(btn => {
            if (btn.textContent.includes('Start Free Trial') || btn.textContent.includes('Get Started')) {
                btn.addEventListener('click', () => this.startTrial());
            }
            if (btn.textContent.includes('Watch Demo') || btn.textContent.includes('Schedule a Demo')) {
                btn.addEventListener('click', () => this.showDemoModal());
            }
        });

        // Alert filters
        document.querySelectorAll('.filter-btn').forEach(btn => {
            btn.addEventListener('click', (e) => this.handleAlertFilter(e));
        });

        // Quick actions
        document.querySelectorAll('.action-btn').forEach(btn => {
            btn.addEventListener('click', (e) => this.handleQuickAction(e));
        });

        // Mobile menu
        const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
        if (mobileMenuBtn) {
            mobileMenuBtn.addEventListener('click', () => this.toggleMobileMenu());
        }
    }

    setupSmoothScrolling() {
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });
    }

    setupAnimations() {
        // Intersection Observer for fade-in animations
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, { threshold: 0.1 });

        // Animate solution cards
        document.querySelectorAll('.solution-card').forEach(card => {
            card.style.opacity = '0';
            card.style.transform = 'translateY(20px)';
            card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            observer.observe(card);
        });

        // Animate analytics cards
        document.querySelectorAll('.analytics-card').forEach(card => {
            card.style.opacity = '0';
            card.style.transform = 'translateX(-20px)';
            card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            observer.observe(card);
        });

        // Animate stats
        document.querySelectorAll('.stat-card').forEach(stat => {
            stat.style.opacity = '0';
            stat.style.transform = 'translateX(-10px)';
            stat.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
            observer.observe(stat);
        });
    }

    async loadAllData() {
        // Simulate API calls with professional data
        await this.simulateAPICall(1200);
        
        this.currentData = {
            employees: {
                employees: [
                    {
                        id: 1,
                        name: "Sarah Chen",
                        department: "Engineering",
                        position: "Senior Software Engineer",
                        hire_date: "2021-03-15",
                        performance_score: 4.7,
                        salary: 125000,
                        email: "sarah.chen@company.com",
                        location: "San Francisco, CA",
                        status: "Active"
                    },
                    {
                        id: 2,
                        name: "Marcus Johnson",
                        department: "Marketing",
                        position: "Marketing Director",
                        hire_date: "2019-07-22",
                        performance_score: 4.5,
                        salary: 110000,
                        email: "marcus.johnson@company.com",
                        location: "New York, NY",
                        status: "Active"
                    }
                ]
            },
            dashboard: {
                summary: {
                    total_employees: 1247,
                    open_positions: 8,
                    pending_leave_requests: 3,
                    active_training_programs: 5,
                    employee_engagement: 87,
                    retention_rate: 94,
                    avg_performance_score: 4.3,
                    high_performers_count: 420
                }
            },
            analytics: {
                churn_predictions: [
                    {
                        employee_name: "Sarah Chen",
                        churn_probability: 78,
                        risk_level: "High"
                    }
                ]
            }
        };
    }

    simulateAPICall(duration) {
        return new Promise(resolve => setTimeout(resolve, duration));
    }

    initializeDashboard() {
        this.updateCurrentDate();
        this.animateStats();
        this.setupRealTimeAlerts();
    }

    updateCurrentDate() {
        const dateElement = document.getElementById('current-date');
        if (dateElement) {
            dateElement.textContent = new Date().toLocaleDateString('en-US', {
                year: 'numeric',
                month: 'long',
                day: 'numeric'
            });
        }
    }

    animateStats() {
        const stats = document.querySelectorAll('.stat-content .value');
        stats.forEach(stat => {
            const finalValue = parseInt(stat.textContent.replace(/,/g, ''));
            this.animateValue(stat, 0, finalValue, 1000);
        });

        // Animate circle charts
        this.animateCircleCharts();
    }

    animateValue(element, start, end, duration) {
        let startTimestamp = null;
        const step = (timestamp) => {
            if (!startTimestamp) startTimestamp = timestamp;
            const progress = Math.min((timestamp - startTimestamp) / duration, 1);
            const value = Math.floor(progress * (end - start) + start);
            element.textContent = value.toLocaleString();
            if (progress < 1) {
                window.requestAnimationFrame(step);
            }
        };
        window.requestAnimationFrame(step);
    }

    animateCircleCharts() {
        const circles = document.querySelectorAll('.circle-chart');
        circles.forEach(circle => {
            const percentage = circle.getAttribute('data-percentage');
            circle.style.background = `conic-gradient(var(--primary) 0% ${percentage}%, var(--border) ${percentage}% 100%)`;
        });
    }

    setupRealTimeAlerts() {
        // Simulate real-time alert updates
        setInterval(() => {
            this.updateAlertStatus();
        }, 30000);
    }

    updateAlertStatus() {
        // Update alert timestamps and status
        const alertTimes = document.querySelectorAll('.alert-time');
        alertTimes.forEach(time => {
            const currentTime = new Date().toLocaleTimeString('en-US', {
                hour: '2-digit',
                minute: '2-digit'
            });
            time.textContent = `Updated ${currentTime}`;
        });
    }

    handleNavigation(e) {
        e.preventDefault();
        const target = e.target.getAttribute('href');
        console.log('Navigation to:', target);
        // Smooth scroll handled by setupSmoothScrolling
    }

    handleTabChange(e) {
        const tabId = e.target.getAttribute('data-tab');
        
        // Update active tab
        document.querySelectorAll('.tab-btn').forEach(tab => {
            tab.classList.remove('active');
        });
        e.target.classList.add('active');

        // Show corresponding content
        document.querySelectorAll('.tab-content').forEach(content => {
            content.classList.remove('active');
        });
        document.getElementById(`${tabId}-tab`).classList.add('active');

        // Load tab-specific data
        this.loadTabData(tabId);
    }

    loadTabData(tabId) {
        switch(tabId) {
            case 'employees':
                this.loadEmployeesData();
                break;
            case 'analytics':
                this.loadAdvancedAnalytics();
                break;
            case 'reports':
                this.loadReportsData();
                break;
        }
    }

    loadEmployeesData() {
        // Load employee management data
        console.log('Loading employees data...');
    }

    loadAdvancedAnalytics() {
        // Load advanced analytics data
        console.log('Loading advanced analytics...');
    }

    loadReportsData() {
        // Load reporting data
        console.log('Loading reports data...');
    }

    handleAlertFilter(e) {
        const filter = e.target.textContent;
        
        // Update active filter
        document.querySelectorAll('.filter-btn').forEach(btn => {
            btn.classList.remove('active');
        });
        e.target.classList.add('active');

        // Filter alerts
        this.filterAlerts(filter);
    }

    filterAlerts(filter) {
        const alerts = document.querySelectorAll('.alert-item');
        
        alerts.forEach(alert => {
            if (filter === 'All') {
                alert.style.display = 'flex';
            } else if (filter === 'High Priority' && alert.classList.contains('high-priority')) {
                alert.style.display = 'flex';
            } else if (filter === 'Compliance' && alert.classList.contains('compliance')) {
                alert.style.display = 'flex';
            } else {
                alert.style.display = 'none';
            }
        });
    }

    handleQuickAction(e) {
        const action = e.target.textContent.trim();
        
        switch(action) {
            case 'Add Employee':
                this.showProfessionalNotification(
                    'Add Employee',
                    'Opening employee creation form...',
                    'info',
                    [
                        { label: 'Open Form', primary: true, handler: 'hrApp.openEmployeeForm()' },
                        { label: 'Cancel', primary: false, handler: 'hrApp.closeNotification()' }
                    ]
                );
                break;
            case 'Generate Report':
                this.showProfessionalNotification(
                    'Generate Report',
                    'Select report type and timeframe',
                    'info',
                    [
                        { label: 'Performance', primary: false, handler: 'hrApp.generatePerformanceReport()' },
                        { label: 'Attendance', primary: false, handler: 'hrApp.generateAttendanceReport()' },
                        { label: 'Cancel', primary: false, handler: 'hrApp.closeNotification()' }
                    ]
                );
                break;
            case 'Schedule Review':
                this.showProfessionalNotification(
                    'Schedule Performance Review',
                    'Choose review period and participants',
                    'info'
                );
                break;
        }
    }

    toggleMobileMenu() {
        const navMenu = document.querySelector('.nav-menu');
        const isVisible = navMenu.style.display === 'flex';
        navMenu.style.display = isVisible ? 'none' : 'flex';
        
        if (!isVisible) {
            navMenu.style.flexDirection = 'column';
            navMenu.style.position = 'absolute';
            navMenu.style.top = '100%';
            navMenu.style.left = '0';
            navMenu.style.right = '0';
            navMenu.style.background = 'white';
            navMenu.style.padding = 'var(--spacing-lg)';
            navMenu.style.boxShadow = 'var(--shadow-lg)';
            navMenu.style.borderTop = '1px solid var(--border)';
        }
    }

    startTrial() {
        this.showProfessionalNotification(
            'Start Free Trial', 
            'Redirecting to trial setup...', 
            'success'
        );
        
        // Simulate redirect
        setTimeout(() => {
            console.log('Redirecting to trial setup...');
        }, 2000);
    }

    showDemoModal() {
        this.showProfessionalNotification(
            'Product Demo', 
            'Opening interactive product demonstration...', 
            'info'
        );
    }

    showProfessionalNotification(title, message, type = 'info', actions = []) {
        const notification = document.createElement('div');
        notification.className = `professional-notification ${type}`;
        
        let actionsHTML = '';
        if (actions.length > 0) {
            actionsHTML = `
                <div class="notification-actions">
                    ${actions.map(action => 
                        `<button class="btn btn-sm ${action.primary ? 'btn-primary' : 'btn-secondary'}" 
                                onclick="(${action.handler})()">
                            ${action.label}
                        </button>`
                    ).join('')}
                </div>
            `;
        }

        notification.innerHTML = `
            <div class="notification-header">
                <h4>${title}</h4>
                <button class="notification-close" onclick="this.parentElement.parentElement.remove()">&times;</button>
            </div>
            <div class="notification-body">
                <p>${message}</p>
            </div>
            ${actionsHTML}
        `;

        // Remove existing notifications
        document.querySelectorAll('.professional-notification').forEach(note => note.remove());
        
        document.body.appendChild(notification);

        // Auto-remove after 8 seconds if no actions
        if (actions.length === 0) {
            setTimeout(() => {
                if (notification.parentElement) {
                    notification.remove();
                }
            }, 8000);
        }
    }

    // Method stubs for notification actions
    openEmployeeForm() {
        console.log('Opening employee form...');
        document.querySelectorAll('.professional-notification').forEach(note => note.remove());
    }

    closeNotification() {
        document.querySelectorAll('.professional-notification').forEach(note => note.remove());
    }

    generatePerformanceReport() {
        this.showProfessionalNotification(
            'Performance Report',
            'Generating Q1 performance report...',
            'success'
        );
        document.querySelectorAll('.professional-notification').forEach(note => note.remove());
    }

    generateAttendanceReport() {
        this.showProfessionalNotification(
            'Attendance Report',
            'Generating monthly attendance report...',
            'success'
        );
        document.querySelectorAll('.professional-notification').forEach(note => note.remove());
    }

    updateCopyrightYear() {
        const yearElement = document.querySelector('.footer-legal span');
        if (yearElement) {
            const currentYear = new Date().getFullYear();
            yearElement.textContent = yearElement.textContent.replace('2024', currentYear.toString());
        }
    }

    loadDemoData() {
        // Demo data is already loaded in loadAllData
        this.initializeDashboard();
    }
}

// Professional Analytics Engine
class ProfessionalAnalytics {
    constructor() {
        this.setupRealTimeUpdates();
        this.setupExportFeatures();
    }

    setupRealTimeUpdates() {
        // Simulate real-time data updates
        setInterval(() => {
            this.updateLiveMetrics();
        }, 30000);
    }

    async updateLiveMetrics() {
        try {
            // In a real app, this would fetch from your backend
            const liveData = {
                totalEmployees: 1247 + Math.floor(Math.random() * 10),
                engagementScore: 87 + Math.floor(Math.random() * 3) - 1
            };
            
            this.updateDashboardMetrics(liveData);
        } catch (error) {
            console.log('Live update failed:', error);
        }
    }

    updateDashboardMetrics(data) {
        // Update metrics with smooth animations
        this.animateMetricUpdate('.stat-card .value', data.totalEmployees);
    }

    animateMetricUpdate(selector, newValue) {
        const elements = document.querySelectorAll(selector);
        elements.forEach(element => {
            const currentValue = parseInt(element.textContent.replace(/,/g, ''));
            if (!isNaN(currentValue)) {
                this.animateValue(element, currentValue, newValue, 1000);
            }
        });
    }

    animateValue(element, start, end, duration) {
        let startTimestamp = null;
        const step = (timestamp) => {
            if (!startTimestamp) startTimestamp = timestamp;
            const progress = Math.min((timestamp - startTimestamp) / duration, 1);
            const value = Math.floor(progress * (end - start) + start);
            element.textContent = value.toLocaleString();
            if (progress < 1) {
                window.requestAnimationFrame(step);
            }
        };
        window.requestAnimationFrame(step);
    }

    setupExportFeatures() {
        // Setup export functionality for reports
        console.log('Export features initialized');
    }
}

// Initialize the application when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.hrApp = new HRApp();
    window.analytics = new ProfessionalAnalytics();
});

// Make methods globally available for HTML onclick handlers
window.openEmployeeForm = () => window.hrApp?.openEmployeeForm?.();
window.closeNotification = () => window.hrApp?.closeNotification?.();
window.generatePerformanceReport = () => window.hrApp?.generatePerformanceReport?.();
window.generateAttendanceReport = () => window.hrApp?.generateAttendanceReport?.();