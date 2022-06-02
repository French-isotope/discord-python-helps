let pkgs = import ./nixpkgs.nix {};
  pythonEnv = pkgs.python3.withPackages(p : [p.numpy p.matplotlib.pyplot p.datetime]);
in pkgs.mkShell {
  buildInputs = [ pythonEnv ];
}
