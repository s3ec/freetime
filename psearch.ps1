$SearchQueries = @(
    "Securing sensitive data on laptops",
    "Pentesting case studies and real-world examples",
    "Healthy habits to adopt in 2024",
    "Gardening tips for beginners",
    "Best low-maintenance plants for indoor gardening",
    "Women's health and nutrition tips",
    "Exercise routines for women at home",
    "Best workout apps for women",
    "Strength training for women",
    "Productivity hacks for working from home",
    "Time management strategies for professionals",
    "Interior design ideas for small spaces",
    "DIY home improvement projects",
    "Creative upcycling ideas for old furniture",
    "Easy vegan breakfast recipes",
    "Vegan meal prep ideas",
    "Plant-based protein sources",
    "Digital minimalism and decluttering your digital life",
    "How to manage and reduce screen time",
    "Benefits of a digital detox",
    "Personal finance tips for beginners",
    "Budgeting strategies for financial success",
    "Investing for beginners",
    "Mindfulness techniques for stress reduction",
    "Self-care practices for mental wellbeing",
    "Building resilience and coping with adversity",
    "Gardening tools and equipment",
    "Organic pest control methods",
    "Raised garden bed ideas",
    "Composting for beginners",
    "Women's mental health resources",
    "Yoga for women's health",
    "Postpartum exercise routines",
    "Balancing work and personal life",
    "Productivity apps and tools",
    "Creating a productive home office",
    "Scandinavian interior design",
    "Repurposing old items for home decor",
    "Quick vegan lunch ideas",
    "Vegan alternatives to popular dishes",
    "Digital minimalism in the workplace",
    "Digital privacy and security",
    "Personal finance podcasts",
    "Financial independence and early retirement",
    "Cognitive-behavioral therapy for stress management",
    "Art therapy for mental wellness",
    "Plant propagation techniques",
    "Container gardening ideas",
    "Vertical gardening for small spaces",
    "Women's reproductive health resources",
    "Pilates exercises for women",
    "Foam rolling exercises for muscle recovery",
    "Morning routines for productivity",
    "Time blocking techniques for better focus",
    "Minimalist interior design",
    "Creating accent walls",
    "Easy vegan dinner recipes",
    "Vegan meal planning",
    "Plant-based meal delivery services",
    "Digital minimalism and social media",
    "Digital detox retreats",
    "Personal finance books",
    "Financial goal setting",
    "Progressive muscle relaxation techniques",
    "Journaling for mental health",
    "Men's health and fitness tips",
    "HIIT workouts for men",
    "Building muscle through proper nutrition",
    "Best men's skincare routines",
    "Fashion tips for men",
    "Men's mental health resources",
    "Hobby ideas for men",
    "Maintaining work-life balance for men"
)


$SearchedQueries = @()

$shell = New-Object -ComObject "WScript.Shell"

foreach ($query in $SearchQueries) {
    if ($SearchedQueries -notcontains $query) {
        $SearchedQueries += $query

        Start-Process msedge 
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