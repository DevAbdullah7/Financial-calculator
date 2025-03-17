from rich.console import Console
from rich.table import Table

console = Console()

table = Table(show_header=True, header_style="bold magenta")
table.add_column("Batch Num", justify="left")
table.add_column("Products", justify="left")
table.add_column("Shipping Price", justify="left")
table.add_column("Profit", justify="left")
table.add_column("Deal Price", justify="left")
table.add_column("Cash", justify="left")

table.add_row(
    "1",
    "49",
    "1,078 SAR",
    "637 SAR",
    "2,401 SAR",
    "1,323 SAR",
)

console.print(table)