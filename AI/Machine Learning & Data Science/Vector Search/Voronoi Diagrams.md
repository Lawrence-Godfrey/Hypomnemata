A **Voronoi diagram** is a way of partitioning space based on a set of points (called _sites_).
- For each site, its **Voronoi cell** is the region of space closer to that site than to any other.
- The boundaries between cells are made up of points equidistant to two (or more) sites.
- In 2D, the boundaries are line segments or rays; in higher dimensions, they’re planes/hyperplanes.
- Dual of the [[Delauny Graphs|Delauny graph]].
### Use Cases
Nearest neighbour search, geographic partitioning (e.g. “closest hospital”), image segmentation, cellular models.
### Intuition
- Imagine dropping several “seeds” onto a flat plane. Then let the seeds spread outward at the same speed. The regions where they first collide become the Voronoi boundaries.
- Useful for nearest neighbour queries, spatial analysis, facility location problems, etc.

![[Pasted image 20250928094450.png|center]]

## Voronoi and Delauny

![[Pasted image 20250928095015.png|center]]
