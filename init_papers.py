papers = [
	"2022-PPIG-33rd-al-madi", 
	"2022-PPIG-33rd-attahiru", 
	"2022-PPIG-33rd-bidlake", 
	"2022-PPIG-33rd-blackwell", 
	"2022-PPIG-33rd-bolzoni", 
	"2022-PPIG-33rd-cortinovis", 
	"2022-PPIG-33rd-crossley", 
	"2022-PPIG-33rd-diapoulis", 
	"2022-PPIG-33rd-gomez", 
	"2022-PPIG-33rd-gopal", 
	"2022-PPIG-33rd-gopal2", 
	"2022-PPIG-33rd-green", 
	"2022-PPIG-33rd-helgesson", 
	"2022-PPIG-33rd-izu", 
	"2022-PPIG-33rd-kiesler", 
	"2022-PPIG-33rd-kiljunen", 
	"2022-PPIG-33rd-lederman", 
	"2022-PPIG-33rd-lieberman", 
	"2022-PPIG-33rd-mccabe", 
	"2022-PPIG-33rd-mclean", 
	"2022-PPIG-33rd-nagle", 
	"2022-PPIG-33rd-nzemeke", 
	"2022-PPIG-33rd-rainer", 
	"2022-PPIG-33rd-rosian", 
	"2022-PPIG-33rd-sarkar", 
	"2022-PPIG-33rd-soderberg", 
	"2022-PPIG-33rd-taylor", 
	"2022-PPIG-33rd-valovy"
]

for paper in papers:
	with open("content/papers/" + paper + '.md', "w") as f:
		f.write("---\n")
		f.write('title: ""\n')
		f.write("authors: []\n")
		f.write('abstract: ""\n')
		f.write("publishedAt: ppig-2022\n")
		f.write("year: 2022\n")
		f.write("url_pdf: /files/" + paper + ".pdf\n")
		f.write("---\n")