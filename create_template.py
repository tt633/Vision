html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Milestone Savings Dashboard</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        
        .header {
            background: white;
            padding: 20px 30px;
            border-radius: 10px;
            margin-bottom: 30px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        .header h1 {
            color: #333;
            font-size: 28px;
        }
        
        .logout-btn {
            background: #667eea;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            text-decoration: none;
            font-size: 14px;
        }
        
        .logout-btn:hover {
            background: #5568d3;
        }
        
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        
        .stat-card {
            background: white;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        .stat-card h3 {
            color: #666;
            font-size: 14px;
            margin-bottom: 10px;
            text-transform: uppercase;
        }
        
        .stat-card .value {
            font-size: 32px;
            font-weight: bold;
            color: #333;
        }
        
        .goals-section {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            margin-bottom: 30px;
        }
        
        .goals-section h2 {
            color: #333;
            margin-bottom: 20px;
        }
        
        .goals-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
        }
        
        .goal-card {
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            padding: 20px;
            transition: transform 0.2s;
        }
        
        .goal-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        
        .goal-card h3 {
            color: #333;
            margin-bottom: 10px;
        }
        
        .goal-card .description {
            color: #666;
            font-size: 14px;
            margin-bottom: 15px;
        }
        
        .progress-bar {
            background: #e0e0e0;
            height: 20px;
            border-radius: 10px;
            overflow: hidden;
            margin-bottom: 10px;
        }
        
        .progress-fill {
            background: linear-gradient(90deg, #667eea, #764ba2);
            height: 100%;
            transition: width 0.3s;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 12px;
            font-weight: bold;
        }
        
        .goal-amounts {
            display: flex;
            justify-content: space-between;
            font-size: 14px;
            color: #666;
        }
        
        .goal-amounts .current {
            color: #667eea;
            font-weight: bold;
        }
        
        .rules-section {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        .rules-section h2 {
            color: #333;
            margin-bottom: 20px;
        }
        
        .rule-item {
            padding: 15px;
            border-left: 4px solid #667eea;
            background: #f8f9fa;
            margin-bottom: 10px;
            border-radius: 5px;
        }
        
        .rule-item h4 {
            color: #333;
            margin-bottom: 5px;
        }
        
        .rule-item .rule-details {
            color: #666;
            font-size: 14px;
        }
        
        .loading {
            text-align: center;
            padding: 40px;
            color: #666;
        }
        
        .empty-state {
            text-align: center;
            padding: 60px 20px;
            color: #999;
        }
        
        .empty-state h3 {
            margin-bottom: 10px;
        }
        
        .btn-primary {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
            font-weight: 600;
            transition: transform 0.2s, box-shadow 0.2s;
            box-shadow: 0 4px 6px rgba(102, 126, 234, 0.4);
        }
        
        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(102, 126, 234, 0.6);
        }
        
        .btn-secondary {
            background: white;
            color: #667eea;
            border: 2px solid #667eea;
            padding: 10px 20px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 14px;
            font-weight: 600;
            transition: all 0.2s;
        }
        
        .btn-secondary:hover {
            background: #667eea;
            color: white;
        }
        
        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.7);
            z-index: 1000;
            align-items: center;
            justify-content: center;
        }
        
        .modal.active {
            display: flex;
        }
        
        .modal-content {
            background: white;
            padding: 40px;
            border-radius: 15px;
            max-width: 600px;
            width: 90%;
            max-height: 90vh;
            overflow-y: auto;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        }
        
        .modal-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 30px;
        }
        
        .modal-header h2 {
            color: #333;
            font-size: 24px;
        }
        
        .close-btn {
            background: none;
            border: none;
            font-size: 28px;
            cursor: pointer;
            color: #999;
            line-height: 1;
        }
        
        .close-btn:hover {
            color: #333;
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        .form-group label {
            display: block;
            margin-bottom: 8px;
            color: #333;
            font-weight: 600;
            font-size: 14px;
        }
        
        .form-group input,
        .form-group select,
        .form-group textarea {
            width: 100%;
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            font-size: 14px;
            transition: border-color 0.2s;
        }
        
        .form-group input:focus,
        .form-group select:focus,
        .form-group textarea:focus {
            outline: none;
            border-color: #667eea;
        }
        
        .form-group textarea {
            resize: vertical;
            min-height: 80px;
        }
        
        .pace-options {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
        }
        
        .pace-option {
            padding: 15px;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            text-align: center;
            cursor: pointer;
            transition: all 0.2s;
        }
        
        .pace-option:hover {
            border-color: #667eea;
        }
        
        .pace-option.selected {
            border-color: #667eea;
            background: #f0f4ff;
        }
        
        .pace-option input[type="radio"] {
            display: none;
        }
        
        .pace-option .pace-name {
            font-weight: 600;
            color: #333;
            margin-bottom: 5px;
        }
        
        .pace-option .pace-desc {
            font-size: 12px;
            color: #666;
        }
        
        .section-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
        }
        
        .rule-type-badge {
            display: inline-block;
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: 600;
            text-transform: uppercase;
        }
        
        .rule-type-badge.recurring {
            background: #e3f2fd;
            color: #1976d2;
        }
        
        .rule-type-badge.habit_reward {
            background: #f3e5f5;
            color: #7b1fa2;
        }
        
        .rule-type-badge.guilty_pleasure_tax {
            background: #fff3e0;
            color: #f57c00;
        }
        
        .goal-card .pace-badge {
            display: inline-block;
            padding: 4px 10px;
            border-radius: 12px;
            font-size: 11px;
            font-weight: 600;
            margin-bottom: 10px;
        }
        
        .goal-card .pace-badge.Conservative {
            background: #e8f5e9;
            color: #2e7d32;
        }
        
        .goal-card .pace-badge.Moderate {
            background: #fff3e0;
            color: #f57c00;
        }
        
        .goal-card .pace-badge.Aggressive {
            background: #ffebee;
            color: #c62828;
        }
        
        .add-rule-section {
            margin-top: 30px;
            padding-top: 30px;
            border-top: 2px solid #e0e0e0;
        }
        
        .add-rule-section h3 {
            color: #333;
            margin-bottom: 20px;
        }
        
        .rule-type-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin-bottom: 20px;
        }
        
        .rule-type-card {
            padding: 20px;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.2s;
            text-align: center;
        }
        
        .rule-type-card:hover {
            border-color: #667eea;
            transform: translateY(-2px);
        }
        
        .rule-type-card.selected {
            border-color: #667eea;
            background: #f0f4ff;
        }
        
        .rule-type-card h4 {
            color: #333;
            margin-bottom: 8px;
            font-size: 16px;
        }
        
        .rule-type-card p {
            color: #666;
            font-size: 13px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎯 Milestone Savings Dashboard</h1>
            <a href="/logout" class="logout-btn">Logout</a>
        </div>
        
        <div class="stats-grid">
            <div class="stat-card">
                <h3>Total Goals</h3>
                <div class="value" id="totalGoals">-</div>
            </div>
            <div class="stat-card">
                <h3>Total Saved</h3>
                <div class="value" id="totalSaved">$0.00</div>
            </div>
            <div class="stat-card">
                <h3>Active Rules</h3>
                <div class="value" id="activeRules">-</div>
            </div>
        </div>
        
        <div class="goals-section">
            <div class="section-header">
                <h2>Your Savings Goals</h2>
                <button class="btn-primary" onclick="openCreateGoalModal()">+ Create New Goal</button>
            </div>
            <div id="goalsContainer" class="loading">Loading goals...</div>
        </div>
        
        <div class="rules-section">
            <div class="section-header">
                <h2>Savings Rules</h2>
                <button class="btn-primary" onclick="openCreateRuleModal()">+ Add Savings Rule</button>
            </div>
            <div id="rulesContainer" class="loading">Loading rules...</div>
        </div>
    </div>
    
    <!-- Create Goal Modal -->
    <div id="createGoalModal" class="modal">
        <div class="modal-content">
            <div class="modal-header">
                <h2>Create New Savings Goal</h2>
                <button class="close-btn" onclick="closeCreateGoalModal()">&times;</button>
            </div>
            <form id="createGoalForm" onsubmit="createGoal(event)">
                <div class="form-group">
                    <label>Goal Name *</label>
                    <input type="text" name="name" required placeholder="e.g., New Laptop, Vacation">
                </div>
                
                <div class="form-group">
                    <label>Target Amount ($) *</label>
                    <input type="number" name="target_amount" step="0.01" required placeholder="e.g., 1500.00">
                </div>
                
                <div class="form-group">
                    <label>Description</label>
                    <textarea name="description" placeholder="What are you saving for?"></textarea>
                </div>
                
                <div class="form-group">
                    <label>Savings Pace *</label>
                    <div class="pace-options">
                        <label class="pace-option">
                            <input type="radio" name="savings_pace" value="Conservative" required>
                            <div class="pace-name">🐢 Conservative</div>
                            <div class="pace-desc">Slow & steady</div>
                        </label>
                        <label class="pace-option">
                            <input type="radio" name="savings_pace" value="Moderate" checked>
                            <div class="pace-name">🚶 Moderate</div>
                            <div class="pace-desc">Balanced approach</div>
                        </label>
                        <label class="pace-option">
                            <input type="radio" name="savings_pace" value="Aggressive">
                            <div class="pace-name">🏃 Aggressive</div>
                            <div class="pace-desc">Fast track</div>
                        </label>
                    </div>
                </div>
                
                <div class="form-group">
                    <label>Image URL (optional)</label>
                    <input type="url" name="image_url" placeholder="https://example.com/image.jpg">
                </div>
                
                <button type="submit" class="btn-primary" style="width: 100%;">Create Goal</button>
            </form>
        </div>
    </div>
    
    <!-- Create Rule Modal -->
    <div id="createRuleModal" class="modal">
        <div class="modal-content">
            <div class="modal-header">
                <h2>Add Savings Rule</h2>
                <button class="close-btn" onclick="closeCreateRuleModal()">&times;</button>
            </div>
            <form id="createRuleForm" onsubmit="createRule(event)">
                <div class="form-group">
                    <label>Rule Name *</label>
                    <input type="text" name="rule_name" required placeholder="e.g., Morning Workout Reward">
                </div>
                
                <div class="form-group">
                    <label>Select Goal *</label>
                    <select name="goal_id" id="ruleGoalSelect" required>
                        <option value="">-- Select a goal --</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label>Rule Type *</label>
                    <div class="rule-type-grid">
                        <label class="rule-type-card">
                            <input type="radio" name="rule_type" value="recurring" required style="display: none;">
                            <h4>💰 Recurring</h4>
                            <p>Automatic regular deposits</p>
                        </label>
                        <label class="rule-type-card">
                            <input type="radio" name="rule_type" value="habit_reward" required style="display: none;">
                            <h4>🎯 Habit Reward</h4>
                            <p>Save when you complete a habit</p>
                        </label>
                        <label class="rule-type-card">
                            <input type="radio" name="rule_type" value="guilty_pleasure_tax" required style="display: none;">
                            <h4>🍕 Guilty Pleasure</h4>
                            <p>Tax on indulgent purchases</p>
                        </label>
                    </div>
                </div>
                
                <div class="form-group">
                    <label>Amount ($) *</label>
                    <input type="number" name="amount" step="0.01" required placeholder="e.g., 5.00">
                </div>
                
                <div class="form-group" id="frequencyGroup" style="display: none;">
                    <label>Frequency *</label>
                    <select name="frequency">
                        <option value="">-- Select frequency --</option>
                        <option value="daily">Daily</option>
                        <option value="weekly">Weekly</option>
                        <option value="monthly">Monthly</option>
                    </select>
                </div>
                
                <div class="form-group" id="categoryGroup" style="display: none;">
                    <label>Trigger Category</label>
                    <input type="text" name="trigger_category" placeholder="e.g., Food Delivery, Entertainment">
                </div>
                
                <button type="submit" class="btn-primary" style="width: 100%;">Create Rule</button>
            </form>
        </div>
    </div>
    
    <script>
        // Fetch and display goals
        async function loadGoals() {
            try {
                const response = await fetch('/api/goals');
                const goals = await response.json();
                
                const container = document.getElementById('goalsContainer');
                
                if (goals.length === 0) {
                    container.innerHTML = '<div class="empty-state"><h3>No goals yet</h3><p>Start by creating your first savings goal!</p></div>';
                    return;
                }
                
                let totalSaved = 0;
                let html = '<div class="goals-grid">';
                
                goals.forEach(goal => {
                    totalSaved += goal.current_amount;
                    const progress = Math.min(goal.progress, 100);
                    
                    html += `
                        <div class="goal-card">
                            <div class="pace-badge ${goal.savings_pace || 'Moderate'}">${goal.savings_pace || 'Moderate'}</div>
                            <h3>${goal.name}</h3>
                            ${goal.description ? `<div class="description">${goal.description}</div>` : ''}
                            <div class="progress-bar">
                                <div class="progress-fill" style="width: ${progress}%">
                                    ${progress.toFixed(0)}%
                                </div>
                            </div>
                            <div class="goal-amounts">
                                <span class="current">$${goal.current_amount.toFixed(2)}</span>
                                <span class="target">/ $${goal.target_amount.toFixed(2)}</span>
                            </div>
                        </div>
                    `;
                });
                
                html += '</div>';
                container.innerHTML = html;
                
                // Update stats
                document.getElementById('totalGoals').textContent = goals.length;
                document.getElementById('totalSaved').textContent = `$${totalSaved.toFixed(2)}`;
            } catch (error) {
                console.error('Error loading goals:', error);
                document.getElementById('goalsContainer').innerHTML = '<div class="empty-state"><h3>Error loading goals</h3></div>';
            }
        }
        
        // Fetch and display savings rules
        async function loadRules() {
            try {
                const response = await fetch('/api/savings-rules');
                const rules = await response.json();
                
                const container = document.getElementById('rulesContainer');
                
                if (rules.length === 0) {
                    container.innerHTML = '<div class="empty-state"><h3>No rules yet</h3><p>Create savings rules to automate your savings!</p></div>';
                    return;
                }
                
                let html = '';
                rules.forEach(rule => {
                    html += `
                        <div class="rule-item">
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <h4>${rule.rule_name}</h4>
                                <span class="rule-type-badge ${rule.rule_type}">${rule.rule_type.replace('_', ' ')}</span>
                            </div>
                            <div class="rule-details">
                                Amount: $${rule.amount.toFixed(2)}
                                ${rule.frequency ? ` | Frequency: ${rule.frequency}` : ''}
                            </div>
                        </div>
                    `;
                });
                
                container.innerHTML = html;
                document.getElementById('activeRules').textContent = rules.length;
            } catch (error) {
                console.error('Error loading rules:', error);
                document.getElementById('rulesContainer').innerHTML = '<div class="empty-state"><h3>Error loading rules</h3></div>';
            }
        }
        
        // Modal functions
        function openCreateGoalModal() {
            document.getElementById('createGoalModal').classList.add('active');
        }
        
        function closeCreateGoalModal() {
            document.getElementById('createGoalModal').classList.remove('active');
            document.getElementById('createGoalForm').reset();
        }
        
        function openCreateRuleModal() {
            loadGoalsForRuleSelect();
            document.getElementById('createRuleModal').classList.add('active');
        }
        
        function closeCreateRuleModal() {
            document.getElementById('createRuleModal').classList.remove('active');
            document.getElementById('createRuleForm').reset();
        }
        
        // Load goals into rule modal select
        async function loadGoalsForRuleSelect() {
            try {
                const response = await fetch('/api/goals');
                const goals = await response.json();
                const select = document.getElementById('ruleGoalSelect');
                select.innerHTML = '<option value="">-- Select a goal --</option>';
                goals.forEach(goal => {
                    select.innerHTML += `<option value="${goal.id}">${goal.name}</option>`;
                });
            } catch (error) {
                console.error('Error loading goals for select:', error);
            }
        }
        
        // Create goal
        async function createGoal(event) {
            event.preventDefault();
            const formData = new FormData(event.target);
            const data = Object.fromEntries(formData);
            
            try {
                const response = await fetch('/api/goals/create', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(data)
                });
                
                if (response.ok) {
                    closeCreateGoalModal();
                    loadGoals();
                    alert('Goal created successfully!');
                } else {
                    alert('Error creating goal');
                }
            } catch (error) {
                console.error('Error:', error);
                alert('Error creating goal');
            }
        }
        
        // Create rule
        async function createRule(event) {
            event.preventDefault();
            const formData = new FormData(event.target);
            const data = Object.fromEntries(formData);
            
            try {
                const response = await fetch('/api/rules/create', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(data)
                });
                
                if (response.ok) {
                    closeCreateRuleModal();
                    loadRules();
                    alert('Rule created successfully!');
                } else {
                    alert('Error creating rule');
                }
            } catch (error) {
                console.error('Error:', error);
                alert('Error creating rule');
            }
        }
        
        // Handle pace option selection
        document.addEventListener('DOMContentLoaded', () => {
            document.querySelectorAll('.pace-option').forEach(option => {
                option.addEventListener('click', function() {
                    document.querySelectorAll('.pace-option').forEach(o => o.classList.remove('selected'));
                    this.classList.add('selected');
                    this.querySelector('input[type="radio"]').checked = true;
                });
            });
            
            // Handle rule type selection
            document.querySelectorAll('.rule-type-card').forEach(card => {
                card.addEventListener('click', function() {
                    document.querySelectorAll('.rule-type-card').forEach(c => c.classList.remove('selected'));
                    this.classList.add('selected');
                    const radio = this.querySelector('input[type="radio"]');
                    radio.checked = true;
                    
                    // Show/hide conditional fields
                    const ruleType = radio.value;
                    document.getElementById('frequencyGroup').style.display = ruleType === 'recurring' ? 'block' : 'none';
                    document.getElementById('categoryGroup').style.display = ruleType === 'guilty_pleasure_tax' ? 'block' : 'none';
                });
            });
            
            // Close modal on outside click
            document.querySelectorAll('.modal').forEach(modal => {
                modal.addEventListener('click', function(e) {
                    if (e.target === this) {
                        this.classList.remove('active');
                    }
                });
            });
        });
        
        // Load data on page load
        window.addEventListener('DOMContentLoaded', () => {
            loadGoals();
            loadRules();
        });
    </script>
</body>
</html>"""

with open("templates/index.html", "w") as f:
    f.write(html_content)

print("templates/index.html created successfully")
