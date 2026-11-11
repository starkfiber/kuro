import {describe,it,expect} from 'vitest';
import {imagePlacement,outputSize} from './kuro-geometry';
describe('Kuro image canvas',()=>{
 it('fits a non-square image without distortion',()=>{expect(imagePlacement(200,100,100,100,'contain')).toEqual({x:0,y:25,width:100,height:50});});
 it('fills and crops at the selected position',()=>{expect(imagePlacement(200,100,100,100,'cover',1,0)).toEqual({x:-100,y:0,width:200,height:100});});
 it('clamps position',()=>{expect(imagePlacement(200,100,100,100,'cover',9,-1)).toEqual({x:-100,y:0,width:200,height:100});});
 it('rejects impossible export sizes',()=>{for(const v of [0,-1,4097,NaN,1.5])expect(()=>outputSize(v,100)).toThrow();expect(outputSize(4096,1)).toEqual({width:4096,height:1});});
});
