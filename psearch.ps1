$SearchQueries = @(
 
    "environmental policies of current administration",
    "congressional approval ratings",
    "foreign policy debates",
    "political campaign fundraising strategies",
    "brexit latest updates",
    "emerging political ideologies",
    "surveillance laws and public opinion",
    "minimum wage debates",
    "social media influence on elections",
    "diplomatic tensions in the Middle East",
    "analysis of state of the union address",
    "voter suppression concerns",
    "impact of fake news in politics",
    "government spending bills 2024",
    "future of healthcare reform",
    "AI technology in political campaigns",
    "climate change policy disagreements",
    "role of social justice movements in politics",
    "immigration reform proposals",
    "global trade negotiations",
    "voting rights legislation updates",
    "foreign aid allocation debates",
    "intelligence community reforms",
    "lobbying regulations",
    "election security concerns",
    "digital privacy laws",
    "cybersecurity threats to elections",
    "government transparency initiatives",
    "surveillance state controversies",
    "campaign finance laws",
    "disinformation campaigns in politics",
    "congressional gridlock analysis",
    "national security strategy shifts",
    "election interference investigations",
    "green energy policies",
    "defense spending debates",
    "role of political satire in public discourse",
    "changing demographics and political landscape",
    "immigration enforcement policies",
    "impact of social media influencers on politics",
    "public perception of political leaders",
    "trade war implications",
    "gun control debates",
    "social welfare programs reform",
    "federal budget deficits analysis",
    "foreign policy alliances",
    "populist movements around the world",
    "advances in election forecasting models",
    "analysis of gerrymandering effects",
    "universal basic income discussions",
    "voting system vulnerabilities",
    "parliamentary procedure controversies",
    "impeachment proceedings updates",
    "constitutional law interpretations",
    "strategic communications in politics",
    "technology regulation debates",
    "role of the judiciary in politics",
    "national emergency declarations critique",
    "polarization in political discourse",
    "civil liberties debates",
    "media bias accusations in politics",
    "terrorism prevention strategies",
    "community policing policies",
    "outer space treaties and politics",
    "corruption scandals in government",
    "education reform proposals",
    "escalating tensions with rival nations",
    "death penalty debates",
    "economic stimulus package analysis",
    "congressional oversight investigations",
    "role of think tanks in policy-making",
    "intelligence sharing agreements",
    "foreign election interference responses",
    "justice system reform efforts",
    "national identity discourse",
    "political satire impact on public opinion",
    "privacy rights legislation updates",
    "voter turnout initiatives",
    "third-party politics outlook",
    "redistricting battles",
    "authoritarianism trends worldwide",
    "role of the media in democracy",
    "campaign trail technology trends",
    "welfare system sustainability concerns",
    "transition to green economy policies",
    "campaign fundraising regulations",
    "political correctness debates",
    "pressure groups influence on policy",
    "election rigging prevention measures",
    "universal healthcare debates",
    "climate change treaties negotiation",
    "criminal justice reform efforts",
    "arms control agreements review",
    "anti-corruption initiatives assessment",
    "foreign military interventions critique",
    "political dynasties impact on governance",
    "youth engagement in politics",
    "digital voting systems security reviews",
    "organizational structure of political parties",
    "energy independence strategies",
    "political TV show analysis",
    "ethnic tensions in global politics",
    "government surveillance oversight",
    "political correctness impact on policy",
    "online disinformation countermeasures",
    "role of independent media in politics",
    "political advertising trends assessment",
    "police reform proposals evaluation",
    "supreme court decisions impact analysis",
    "voter registration accessibility reviews",
    "defense policy shifts assessment",
	"election predictions 2024",
    "COVID-19 impact on voting trends",
    "latest scandals in congress",
    "new immigration policies",
    "speeches by world leaders",
    "vote counting software controversies",
    "presidential debate schedules 2024",
    "role of faith in politics",
    "trade agreements impact on economy",
    "anti-terrorism strategies effectiveness",
    "political rhetoric analysis",
    "environmental protection policies evaluation"
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