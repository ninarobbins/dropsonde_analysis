from quickgrid import *from plots import *from datetime import datetimeimport globflight_time = datetime(2024, 8, 22, 12, 0, 0)flight_id = "20240822"# Flight directory# dropsonde_dir = "/Users/ninarobbins/Desktop/PhD/ORCESTRA/HALO-DATA"dropsonde_dir = f"/Users/ninarobbins/Desktop/PhD/ORCESTRA/HALO-DATA/{flight_time.strftime("%Y%m%d")}"# Flight datasetdropsonde_ds = grid_together(dropsonde_dir)dropsonde_ds = derived_products(dropsonde_ds)# Plots# Plot RH for L1 datadropsonde_ds_atr = dropsonde_ds.sel(launch_time=slice("2024-08-22T18:30", "2024-08-22T20:00"))# launch_locations_map(dropsonde_ds_atr, dropsonde_dir, flight_id)# profiles(dropsonde_ds_atr, dropsonde_dir, flight_id)all_quicklook_plots(dropsonde_ds, dropsonde_dir, flight_id)