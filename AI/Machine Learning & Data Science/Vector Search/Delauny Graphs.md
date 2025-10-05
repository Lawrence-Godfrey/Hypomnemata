### Delaunay Triangulation
The **Delaunay triangulation** is the _dual graph_ of the [[Voronoi Diagrams|Voronoi diagram]].
- Connect two sites with an edge if their Voronoi cells share a boundary.
- In 2D, this produces a triangulation (a set of non-overlapping triangles) covering the convex hull of the points.
### Use Cases
Mesh generation, interpolation (esp. natural neighbour interpolation), computer graphics, finite element methods.
### Properties
- Maximises the minimum angle of all the angles in the triangulation (avoids skinny triangles).
- Equivalent to saying: for each triangle in the triangulation, the **circumcircle** of that triangle contains no other points from the set inside it.
- In higher dimensions, it generalises to simplices (tetrahedra, etc.).

## Voronoi and Delauny

![[Pasted image 20250928095015.png|center]]
