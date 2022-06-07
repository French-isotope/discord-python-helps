let pkgs = import ./nixpkgs-3d_cube.nix {};
  pythonEnv = pkgs.python3.withPackages(p : [p.numpy p.matplotlib]);
in pkgs.mkShell {
  buildInputs = [ pythonEnv ];
}
