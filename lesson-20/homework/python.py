# 1
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect("chinook.db")

# Load necessary tables into pandas
customers = pd.read_sql("SELECT CustomerId, FirstName, LastName FROM Customer", conn)
invoices = pd.read_sql("SELECT InvoiceId, CustomerId, Total FROM Invoice", conn)

# Total amount spent per customer
customer_totals = invoices.groupby("CustomerId")["Total"].sum().reset_index()

# Merge with customer names
customer_totals = customer_totals.merge(customers, on="CustomerId")
customer_totals["CustomerName"] = customer_totals["FirstName"] + " " + customer_totals["LastName"]

# Sort and get top 5
top5_customers = customer_totals.sort_values("Total", ascending=False).head(5)

# Display results
print(top5_customers[["CustomerId", "CustomerName", "Total"]])
# 2
# Load more tables
invoice_lines = pd.read_sql("SELECT InvoiceLineId, InvoiceId, TrackId FROM InvoiceLine", conn)
tracks = pd.read_sql("SELECT TrackId, AlbumId FROM Track", conn)

# Merge to get album info in invoice lines
invoice_lines_tracks = invoice_lines.merge(tracks, on="TrackId")
invoices = pd.read_sql("SELECT InvoiceId, CustomerId FROM Invoice", conn)

# Add customer info to each invoice line
purchases = invoice_lines_tracks.merge(invoices, on="InvoiceId")

# Group tracks purchased by each customer by album
customer_album_tracks = purchases.groupby(["CustomerId", "AlbumId"])["TrackId"].nunique().reset_index(name="TracksPurchased")

# Get total number of tracks in each album
album_track_counts = tracks.groupby("AlbumId")["TrackId"].nunique().reset_index(name="TotalTracks")

# Merge to compare purchased vs available tracks
purchase_comparison = customer_album_tracks.merge(album_track_counts, on="AlbumId")

# Identify full album purchases
purchase_comparison["FullAlbum"] = purchase_comparison["TracksPurchased"] == purchase_comparison["TotalTracks"]

# If customer has *any* full album purchase, they are full album buyer
full_album_customers = purchase_comparison.groupby("CustomerId")["FullAlbum"].any().reset_index()

# Categorize customers
full_album_customers["Preference"] = full_album_customers["FullAlbum"].apply(lambda x: "Full Albums" if x else "Individual Tracks")

# Summary percentage
preference_summary = full_album_customers["Preference"].value_counts(normalize=True) * 100
print(preference_summary.round(2))
