{
  description = "Python Dev Environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
  flake-utils.lib.eachDefaultSystem (system:
    let
      pkgs = nixpkgs.legacyPackages.${system};
    in
    {
      devShells.default = pkgs.mkShell {
        packages = with pkgs; [
          python312
          python312Packages.ipython
          python312Packages.pytest

          python312Packages.black
          python312Packages.ruff
          python312Packages.mypy

          act
          pre-commit
        ];

        shellHook = ''
          echo "Loaded dev environment."

          if [ -e .pre-commit-config.yaml ]; then
            pre-commit install
          else
            echo "Warning: No .pre-commit-config.yaml found"
          fi
        '';
      };
    }
  );
}
