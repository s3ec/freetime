$SearchQueries = @(
    "Securing sensitive data on laptops",
    "Pentesting case studies and real-world examples",
    "Mastering command-line tools for pentesting",
    "Effective report writing in penetration testing",
    "Boosting productivity with Windows search tips",
    "Securing laptops in public Wi-Fi environments",
    "Pentesting challenges and competitions",
    "Windows shortcuts to navigate files and folders efficiently",
    "Mobile device security for improved productivity",
    "Advanced techniques for wireless network pentesting",
    "Using virtual machines for pentesting",
    "Windows shortcuts for instant access to settings",
    "Securing laptops against physical theft",
    "Pentesting in enterprise environments",
    "Boosting productivity with workspace organization",
    "Social engineering tactics in pentesting",
    "Windows keyboard shortcuts for power users",
    "Pentesting engagements: scoping and execution",
    "Tips for secure online browsing on laptops",
    "Continuous learning in the field of pentesting",
    "Customizing Windows shortcuts for personal workflow",
    "Pentesting IoT devices for vulnerabilities",
    "Securing Windows laptops with encryption",
    "How to create a pentesting lab environment",
    "Windows shortcuts for efficient application switching",
    "Pentesting techniques for identifying security weaknesses",
    "Workstation ergonomics for increased productivity",
    "Pentesting best practices for software developers",
    "Windows keyboard shortcuts for quick access to programs",
    "Best budgeting apps for 2024",
    "Top vacation destinations in Europe",
    "Healthy recipes for weight loss",
    "Latest fashion trends for fall 2024",
    "Upcoming Marvel movies in 2024",
    "How to start investing in stocks",
    "New iPhone features in the latest update",
    "How to improve your credit score",
    "Workout routines for beginners",
    "Best places to visit in Japan",
    "Home workouts without equipment",
    "Tips for better sleep at night",
    "Productivity hacks for students",
    "New video games 2024",
    "Best TV shows to binge-watch",
    "How to build a gaming PC",
    "Recipes for beginners",
    "Popular interior design trends",
    "Tips for working from home effectively",
    "Travel hacks for saving money",
    "Healthy lunch ideas",
    "Upcoming music festivals 2024",
    "Beginner's guide to meditation",
    "DIY home improvement projects",
    "How to negotiate a salary increase",
    "Best books to read in 2024",
    "Low-carb dinner recipes",
    "How to start a podcast",
    "Summer fashion essentials",
    "Best gadgets of 2024",
    "Guide to buying a house",
    "Self-care tips for busy professionals",
    "Easy coding projects for beginners",
    "Top universities in the world",
    "How to grow an indoor garden",
    "Tips for mastering time management",
    "Budget-friendly meal prep ideas",
    "Latest beauty trends",
    "How to choose the right career path",
    "Remote work job opportunities",
    "Tips for improving public speaking skills",
    "Healthy snacks for weight loss",
    "Upcoming concerts near me",
    "Beginner's guide to yoga",
    "Nutritious breakfast ideas",
    "Fashion trends for men in 2024",
    "Popular podcasts of the year",
    "How to start a side hustle",
    "Tips for reducing stress and anxiety",
    "Best personal finance apps",
    "New tech gadgets for home",
    "How to create a resume",
    "Best online learning platforms",
    "Easy dessert recipes",
    "Cocktail recipes for beginners",
    "Home office setup ideas",
    "Guide to sustainable living",
    "Parenting tips for new parents",
    "How to organize your closet effectively",
    "Tips for improving memory",
    "Travel essentials for a trip",
    "Celebrity gossip and news",
    "How to handle difficult coworkers",
    "New workout trends",
    "How to plan a wedding on a budget",
	"How to lose weight quickly",
	 "Keyboard shortcuts for faster typing",
    "Productivity tools for remote work",
    "How to set up dual monitors for increased productivity",
    "Efficient ways to organize digital files",
    "Windows shortcuts for improved workflow",
    "Tips to speed up your laptop performance",
    "Best laptops for multitasking and productivity",
    "Maximizing productivity with time management techniques",
    "Essential software for pentesting beginners",
    "Learning resources for ethical hacking and pentesting",
    "Common pentesting tools and their uses",
    "Cybersecurity certifications for aspiring pentesters",
    "Pentesting methodologies and best practices",
    "Network scanning techniques in penetration testing",
    "How to secure Windows systems against cyber threats",
    "Keyboard shortcuts to boost Windows productivity",
    "Penetration testing in cloud computing environments",
    "Improving efficiency with laptop keyboard shortcuts",
    "Automation tools for pentesters",
    "Cybersecurity challenges in IoT devices",
    "Enhancing productivity with task management apps",
    "Windows shortcuts for power users",
    "Best practices for pentesting web applications",
    "Best podcasts for motivation",
    "Healthy habits to adopt in 2024"
)

$SearchedQueries = @()

$shell = New-Object -ComObject "WScript.Shell"

foreach ($query in $SearchQueries) {
    if ($SearchedQueries -notcontains $query) {
        $SearchedQueries += $query

        Start-Process msedge "https://www.bing.com"
        Start-Sleep -Seconds 5

        $shell.AppActivate('Microsoft Edge')

        Start-Sleep -Seconds 1
        $shell.SendKeys($query)
        $shell.SendKeys("{ENTER}")

        $DelaySeconds = Get-Random -Minimum 5 -Maximum 15
        Write-Host "Searching for '$query'. Waiting for $DelaySeconds seconds before the next search..."
        Start-Sleep -Seconds $DelaySeconds

        Stop-Process -Name msedge
    } else {
        Write-Host "Skipping already searched query: $query"
    }
}